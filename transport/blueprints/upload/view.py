# -*- coding: utf-8 -*-
'''
    :file: upload.py
    :author: -Farmer
    :url: https://blog.farmer233.top
    :date: 2022/05/26 13:16:47
'''

# type
from werkzeug.datastructures import FileStorage
from io import BytesIO

from flask import current_app
from transport.blueprints.upload.schema import UploadSchema
from transport.common.extensions import cache
from . import upload_bp

@cache.memoize(timeout=30)
def set_cache_file(file_name:str, file:bytes) -> bytes:
    print(file_name, file)
    return file


@upload_bp.post("/")
@upload_bp.input(UploadSchema, location="files")
def upload(data:dict):
    print(data, type(data))
    print(data.get("file"), type(data.get("file")))
    file:FileStorage = data.get("file")
    result = set_cache_file(file_name=file.name, file=file.stream)
    print("result",result, type(result))
    return "upload"