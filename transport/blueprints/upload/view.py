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
from transport.common.utils import generate_extract_code
from . import upload_bp

def create_md5_code(md5, timeout) -> int:
    retry = current_app.config.get("RETRY", 3)

    for _ in range(retry):
        extract_code = generate_extract_code()
        if cache.add(extract_code, md5, timeout):
            print(extract_code, md5)
            # 只有成功设置提取码，才映射 md -> 提取码的关系
            code_prefix = current_app.config.get("CODE_PREFIX", "extract_code")
            status = cache.add(f"{code_prefix}:{md5}", extract_code, timeout)
            print(status)
            return extract_code

    raise GenerateException

def get_extract_code_with_md5(md5):
    code_prefix = current_app.config.get("CODE_PREFIX", "extract_code")
    return cache.get(f"{code_prefix}:{md5}")


def set_cache_file(file_md5, file_name: str, file: bytes, **kwargs) -> int:
    timeout = int(current_app.config.get("CACHE_DEFAULT_TIMEOUT", 10))
    # 校验缓存层是否已经存在该数据
    test = cache.add(file_md5, file, timeout=timeout)
    print(test)
    if test:
        # 生成提取码 & 添加提取码与 md5 的映射关系
        return create_md5_code(md5=file_md5, timeout=timeout)
    # 查找文件的提取码
    return get_extract_code_with_md5(file_md5)        

class FileView(MethodView):
    pass


@upload_bp.get("/")
def get_random():
    return f"{generate_extract_code()}"

@upload_bp.get("/show/<key>")
def show(key):
    code_prefix = current_app.config.get("CODE_PREFIX", "extract_code")
    all = cache.get_dict(f"{key}")
    print(all)
    print(cache.get_many(f"{key}"))
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
    extract_code = set_cache_file(file_md5=file_md5,
                file_name=secure_filename(file.filename), file=file.stream.read())

    return {"extract_code": extract_code}