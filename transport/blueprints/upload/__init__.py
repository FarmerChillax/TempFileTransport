# -*- coding: utf-8 -*-
'''
    :file: __init__.py
    :author: -Farmer
    :url: https://blog.farmer233.top
    :date: 2022/06/18 17:33:27
'''
from apiflask import APIBlueprint

ver = '/api/v1'

upload_bp = APIBlueprint("Upload", __name__, url_prefix=ver + "/upload")

from . import view