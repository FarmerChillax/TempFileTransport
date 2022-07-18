# -*- coding: utf-8 -*-
'''
    :file: __init__.py
    :author: -Farmer
    :url: https://blog.farmer233.top
    :date: 2022/05/24 12:25:25
'''
import click
from apiflask import APIFlask
from transport.common.config import config
from transport.common.extensions import db, cors, token_auth, cache


def create_app(config_name:str = "development")->APIFlask:
    app = APIFlask(__name__, title="FileTransport", version='0.1.0')

    # load config
    app.config.from_object(config[config_name])

    # init extension
    register_extensions(app=app)
    # register buleprint
    register_buleprints(app=app)
    # 
    return app


def register_buleprints(app:APIFlask):
    from transport.blueprints import upload_bp, download_bp
    app.register_blueprint(upload_bp)
    app.register_blueprint(download_bp)


def register_extensions(app: APIFlask):
    ''' 初始化扩展 '''
    db.init_app(app=app)
    cors.init_app(app=app)
    cache.init_app(app=app)


def register_commands(app: APIFlask):
    """注册cli函数"""
    @app.cli.command()
    def initdb():
        db.create_all()
        click.echo("init database.")

    @app.cli.command()
    def dropdb():
        db.drop_all()
        click.echo("drop database.")
