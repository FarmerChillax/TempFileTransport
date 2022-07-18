# -*- coding: utf-8 -*-
'''
    :file: __init__.py
    :author: -Farmer
    :url: https://blog.farmer233.top
    :date: 2022/07/14 22:07:33
'''
from apiflask import APIBlueprint

ver = '/api/v1'

download_bp = APIBlueprint("Download", __name__, url_prefix=ver + "/download")

from . import view