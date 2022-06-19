# -*- coding: utf-8 -*-
'''
    :file: auth.py
    :author: -Farmer
    :url: https://blog.farmer233.top
    :date: 2022/05/24 17:17:15
'''
from flask_httpauth import HTTPTokenAuth

token_auth = HTTPTokenAuth()



@token_auth.verify_token
def verify_token(token:str):
    pass