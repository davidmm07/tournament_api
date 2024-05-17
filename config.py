#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# ENV = 'run' to run the app or 'test' to run the tests
ENV = 'run'


class Config:
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DATABASE_CONNECT_OPTIONS = {}
    SECRET_KEY = 'SuperSecretKey' #TODO Change for ENV
    THREADS_PER_PAGE = 8

class ConfigTest:
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'test_app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TESTING = True
    SECRET_KEY = 'SuperSecretKey' #TODO Change for ENV
    THREADS_PER_PAGE = 8