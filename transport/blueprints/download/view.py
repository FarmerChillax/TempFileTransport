# -*- coding: utf-8 -*-
'''
    :file: view.py
    :author: -Farmer
    :url: https://blog.farmer233.top
    :date: 2022/07/14 22:07:55
'''
from transport.common.utils import TempFile
from . import download_bp


@download_bp.get("/<key>")
def download(key:int):
    return TempFile.get_download_file(key)