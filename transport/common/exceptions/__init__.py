# -*- coding: utf-8 -*-
'''
    :file: __init__.py
    :author: -Farmer
    :url: https://blog.farmer233.top
    :date: 2022/07/18 23:31:36
'''

class GenerateException(Exception):
    
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
    
    def __repr__(self) -> str:
        return f"提取码生成失败"