#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, abort, session, request
from jinja2 import TemplateNotFound
from flask_socketio import SocketIO, send, emit
from web_core import create_app

app = create_app()
socket_io = SocketIO(app)

im_bp = Blueprint('im_bp', __name__, template_folder='templates')


