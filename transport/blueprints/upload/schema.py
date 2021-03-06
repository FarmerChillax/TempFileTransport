# -*- coding: utf-8 -*-
'''
    :file: schema.py
    :author: -Farmer
    :url: https://blog.farmer233.top
    :date: 2022/07/13 22:56:50
'''
from apiflask import Schema
from apiflask.fields import File, String

class UploadSchema(Schema):
    md5 = String()
    file = File()