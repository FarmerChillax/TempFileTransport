# -*- coding: utf-8 -*-
'''
    :file: utils.py
    :author: -Farmer
    :url: https://blog.farmer233.top
    :date: 2022/07/14 22:38:42
'''
from ast import Str
import typing as t
from io import BytesIO
from random import randint
from flask import current_app, send_file
from transport.common.exceptions import GenerateException
from transport.common.extensions import cache

def generate_extract_code():
    """生成提取码

    Returns:
        int: 提取码
    """
    return randint(1000, 10000)


class TempFile():

    def __init__(self, md5:str, filename:str, file_stream:t.Union[bytes,BytesIO], timeout:int = None) -> None:
        self.md5 = md5
        self.filename = filename
        self.file_stream = file_stream
        self.timeout = timeout or int(current_app.config.get('CACHE_DEFAULT_TIMEOUT', 3600))

    @staticmethod
    def get_download_file(code:str):
        code_to_md5_key = f"{current_app.config.get('PREFIX_CODE_TO_MD5')}:{code}"
        md5 = cache.get(code_to_md5_key)
        if md5 == None:
            raise FileNotFoundError

        md5_to_filename_key = f"{current_app.config.get('PREFIX_MD5_TO_FILENAME')}:{md5}"
        filename = cache.get(md5_to_filename_key)
        md5_to_file_key = f"{current_app.config.get('PREFIX_MD5_TO_FILE')}:{md5}"
        file = cache.get(md5_to_file_key)

        return send_file(BytesIO(file), as_attachment=True, download_name=filename)


    def save(self) -> str:
        # 已经缓存，返回提取码
        pre_check = self._save_pre_check()
        if pre_check != None:
            return pre_check

        extract_code = self.__set_code_to_md5()
        # 设置 md5 -> 提取码 的缓存
        md5_to_code_key:str = f'{current_app.config.get("PREFIX_MD5_TO_CODE")}:{self.md5}'
        if not cache.add(md5_to_code_key, extract_code, self.timeout):
            # logger
            raise  
        # 设置 md5 -> 文件 的缓存
        md5_to_file_key: str = f'{current_app.config.get("PREFIX_MD5_TO_FILE")}:{self.md5}'
        # 校验缓存层是否已经存在该数据
        if not cache.add(md5_to_file_key, self.file_stream, self.timeout):
            # logger
            raise
        # 设置 md5 -> filename 的缓存
        md5_to_filename_key:str = f'{current_app.config.get("PREFIX_MD5_TO_FILENAME")}:{self.md5}'
        if not cache.add(md5_to_filename_key, self.filename, self.timeout):
            # logger
            raise

        return extract_code

    def _save_pre_check(self):
        md5_to_code_key:str = f'{current_app.config.get("PREFIX_MD5_TO_CODE")}:{self.md5}'
        return cache.get(md5_to_code_key)

    def __set_code_to_md5(self) -> str:
        for _ in range(3):
            extract_code:str = str(generate_extract_code())
            code_to_md5_key:str = f'{current_app.config.get("PREFIX_CODE_TO_MD5")}:{extract_code}'
            if cache.add(code_to_md5_key, self.md5, self.timeout):
                return extract_code

        raise GenerateException
