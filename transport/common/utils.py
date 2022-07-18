# -*- coding: utf-8 -*-
'''
    :file: utils.py
    :author: -Farmer
    :url: https://blog.farmer233.top
    :date: 2022/07/14 22:38:42
'''

from random import randint


def generate_extract_code():
    """生成提取码

    Returns:
        int: 提取码
    """
    return randint(1000, 10000)