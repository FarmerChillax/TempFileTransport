# -*- coding: utf-8 -*-
'''
    :file: upload.py
    :author: -Farmer
    :url: https://blog.farmer233.top
    :date: 2022/05/26 13:16:47
'''
from logging import raiseExceptions
from os import stat
from time import time
from werkzeug.datastructures import FileStorage
from werkzeug.utils import secure_filename
from io import BytesIO

from flask import current_app
from flask.views import MethodView
from transport.blueprints.upload.schema import UploadSchema
from transport.common.exceptions import GenerateException
from transport.common.extensions import cache
from transport.common.utils import TempFile, generate_extract_code
from . import upload_bp



@upload_bp.get("/show/<key>")
def show(key):
    code_prefix = current_app.config.get("PREFIX_CODE_TO_MD5")
    all = cache.get_dict(f"{code_prefix}:{key}")
    print(all)
    return f"{all}"


@upload_bp.post("/")
@upload_bp.input(UploadSchema, location="files")
def upload(data: dict):
    """上传文件 api

    Args:
        data (dict): requestBody

    Returns:
        dict: 返回md5、生成的提取码等信息
    """
    file: FileStorage = data.get("file")
    file_md5 = data.get("md5")
    # 缓存文件
    temp_file = TempFile(md5=file_md5, filename=secure_filename(file.filename), file_stream=file.stream.read())
    extract_code = temp_file.save()
    return {"extract_code": extract_code}