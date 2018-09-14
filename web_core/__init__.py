#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DEBUG=True,
        SQLALCHEMY_DATABASE_URI='mysql+mysqldb://root:dev2312@127.0.0.1:3306/walle?charset=utf8',
        SQLALCHEMY_POOL_RECYCLE=10,
        SQLALCHEMY_POOL_TIMEOUT=10,
        SQLALCHEMY_POOL_SIZE=5,
        SQLALCHEMY_TRACK_MODIFICATIONS=True,
    )

    from web_core.im.views import im_bp
    app.register_blueprint(im_bp)

    return app
