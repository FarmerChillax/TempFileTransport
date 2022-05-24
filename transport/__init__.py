# -*- coding: utf-8 -*-
'''
    :file: __init__.py
    :author: -Farmer
    :url: https://blog.farmer233.top
    :date: 2022/05/24 12:25:25
'''
from apiflask import APIFlask

def make_app(config_name:str = None)->APIFlask:
    app = APIFlask(__name__, title="FileTransport", version='0.1.0')

    # load config

    # init extension

    # register buleprint

    # 
    return app


def register_buleprints(app:APIFlask):
    # app.register_blueprint()
    pass
