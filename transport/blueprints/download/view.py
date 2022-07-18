# -*- coding: utf-8 -*-
'''
    :file: view.py
    :author: -Farmer
    :url: https://blog.farmer233.top
    :date: 2022/07/14 22:07:55
'''
from io import BytesIO
from tempfile import SpooledTemporaryFile
from flask import send_file
from sqlalchemy import true
from transport.common.extensions import cache
from . import download_bp

def get_file_with_cache(key):
    return cache.get(key)

@download_bp.get("/<key>")
def download(key:int):
    data = get_file_with_cache(key=key)
    return send_file(BytesIO(data), as_attachment=true, download_name=key)