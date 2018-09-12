#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import DateTime, Column, func
from web_core import app

db = SQLAlchemy(app)
db_session = db.session


def timestamp_mixin(cls):
    """
    Model column: timestamp mixin decorator.
    """

    cls.created_at = Column(DateTime, default=func.now(), nullable=False)
    cls.updated_at = Column(DateTime, default=func.now(), nullable=False)

    return cls