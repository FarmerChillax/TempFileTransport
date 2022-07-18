# -*- coding: utf-8 -*-
'''
    :file: schema.py
    :author: -Farmer
    :url: https://blog.farmer233.top
    :date: 2022/07/14 22:08:42
'''

from apiflask import Schema
from apiflask.fields import File

class DownloadSchema(Schema):
    file = File()