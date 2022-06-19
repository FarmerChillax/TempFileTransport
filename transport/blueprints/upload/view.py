# -*- coding: utf-8 -*-
'''
    :file: upload.py
    :author: -Farmer
    :url: https://blog.farmer233.top
    :date: 2022/05/26 13:16:47
'''

from io import BytesIO

from flask import current_app
from transport.common.extensions import cache
from . import upload_bp

@cache.memoize(timeout=current_app.config.get("EXPIRE_TIME", 3600 * 24))
def set_cache_file(file_name:str, file:bytes) -> bytes:
    return file

@upload_bp.post("/")
def upload():
    # BytesIO()
    return "upload"