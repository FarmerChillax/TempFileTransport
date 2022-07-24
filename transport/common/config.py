# -*- coding: utf-8 -*-
'''
    :file: config.py
    :author: -Farmer
    :url: https://blog.farmer233.top
    :date: 2022/06/18 17:23:23
'''
from datetime import date
import os
import sys

basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


# SQLite URI compatible
WIN = sys.platform.startswith('win')
if WIN:
    prefix = 'sqlite:///'
else:
    prefix = 'sqlite:////'

# 基本配置
class BaseConfig(object):
    # 鉴权加密密钥（cookie）
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev key')
    # ORM框架配置
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    EXPIRE_TIME = 3600 * 24
    # expire
    # 缓存设置
    CACHE_TYPE = os.getenv("CACHE_TYPE", 'redis')
    CACHE_DIR = "./cache"
    CACHE_DEFAULT_TIMEOUT = os.getenv("CACHE_DEFAULT_TIMEOUT", 3600)
    CACHE_REDIS_URL = os.getenv("CACHE_REDIS_URL", 'redis://username:password@localhost:6379')

    # 前缀设置
    PREFIX_MD5_TO_FILE = os.getenv("PREFIX_MD5_TO_FILE", "MD5_TO_FILE")
    PREFIX_MD5_TO_FILENAME = os.getenv("PREFIX_MD5_TO_FILENAME", "MD5_TO_FILENAME")
    PREFIX_MD5_TO_CODE = os.getenv("PREFIX_MD5_TO_CODE", "MD5_TO_CODE")
    PREFIX_CODE_TO_MD5 = os.getenv("PREFIX_CODE_TO_MD5", "CODE_TO_MD5")


# 开发环境配置
class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_ECHO = True
    # 开发环境使用sqlite作为开发数据库
    SQLALCHEMY_DATABASE_URI = os.getenv(
        'DATABASE_URL', prefix + os.path.join(basedir, 'data.db'))

# 测试配置
class TestingConfig(BaseConfig):
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'  # in-memory database

# 生产环境配置
class ProductionConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.getenv(
        'DATABASE_URL', prefix + os.path.join(basedir, 'data.db'))
    SQLALCHEMY_POOL_RECYCLE = 280


# export配置
config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}
