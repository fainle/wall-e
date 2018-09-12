#!/usr/bin/env python
# -*- coding: utf-8 -*-

from web_core.model import db, timestamp_mixin
from sqlalchemy import Column, Integer, String, Text


class Corpus(db.Model):
    __tablename__ = 'corpus'

    id = Column(Integer, primary_key=True)
    type = Column(Integer, default=0)
    q = Column(String(255))
    a = Column(String(255))
    times = Column(Integer, default=1)

    def __repr__(self):
        return "<Corpus('%s','%s','%s','%s','%s')>" % (self.id, self.type, self.q, self.a, self.times)