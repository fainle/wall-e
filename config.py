#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Config(object):
    DEBUG = False
    TESTING = False


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql://user@localhost/foo'


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://root:dev2312@127.0.0.1:3306/walle?charset=utf8'
    SQLALCHEMY_POOL_RECYCLE = 10
    SQLALCHEMY_POOL_TIMEOUT = 10
    SQLALCHEMY_POOL_SIZE = 5
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql://user@localhost/foo'
    TESTING = True