#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import render_template, session, abort, request
from flask_socketio import SocketIO, emit
from web_core import create_app

app = create_app()
socket_io = SocketIO(app)


@app.route('/')
def im_index():
    return render_template('im/index.html')


@socket_io.on('connection', namespace='/chat')
def user_connected():
    print('User connected')


# When the client emits 'new message', this listens and executes
@socket_io.on('new message', namespace='/chat')
def new_message(data):
    emit('new message', {'username': session['username'], 'message': data}, broadcast=True)


# When client emits 'add user' this listens and executes
@socket_io.on('add user', namespace='/chat')
def add_user(data):
    global usernames
    global number_of_users

    session['username'] = data
    usernames[data] = session['username']

    number_of_users += 1;

    emit('login', {'numUsers': number_of_users})
    emit('user joined', {'username': session['username'], 'numUsers': number_of_users}, broadcast=True)


@socket_io.on('typing', namespace='/chat')
def typing_response():
    try:
        emit('typing', {'username': session['username']}, broadcast=True)
    except:
        pass


@socket_io.on('stop typing', namespace='/chat')
def stop_typing():
    try:
        emit('stop typing', {'username': session['username']}, broadcast=True)
    except:
        pass


@socket_io.on('disconnect', namespace='/chat')
def disconnect():
    global usernames
    global number_of_users

    try:
        del usernames[session['username']]
        number_of_users -= 1
        emit('user left', {'username': session['username'], 'numUsers': number_of_users}, broadcast=True)

    except:
        pass


if __name__ == '__main__':
    socket_io.run(app)