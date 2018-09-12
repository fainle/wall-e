#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import DateTime, Column, func

app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')

db = SQLAlchemy(app)
Base = db.Model
db_session = db.session


def timestamp_mixin(cls):
    """
    Model column: timestamp mixin decorator.
    """

    cls.created_at = Column(DateTime, default=func.now(), nullable=False)
    cls.updated_at = Column(DateTime, default=func.now(), nullable=False)

    return cls