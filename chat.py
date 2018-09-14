#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask_socketio import SocketIO
from web_core.im.views import im_bp
from web_core import create_app

app = create_app()
app.register_blueprint(im_bp)

socket_io = SocketIO(app)

if __name__ == '__main__':
    socket_io.run(app)
