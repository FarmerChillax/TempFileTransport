# -*- coding: utf-8 -*-
'''
    :file: extensions.py
    :author: -Farmer
    :url: https://blog.farmer233.top
    :date: 2022/05/24 17:15:58
'''
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from .auth import token_auth

cors = CORS()
db = SQLAlchemy()

