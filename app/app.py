#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from config import ENV
from flask_migrate import Migrate

from app.views.monsters import monsters_bp 
from app.views.battles import battles_bp 

def create_app():
    app = Flask(__name__)

    if ENV == 'test':
        app.config.from_object('config.ConfigTest')
    else:
        app.config.from_object('config.Config')

    # create db connection
    db = SQLAlchemy(app)
    migrate = Migrate(app, db)
    ma = Marshmallow(app)

    app.register_blueprint(monsters_bp, url_prefix='/monsters')
    app.register_blueprint(battles_bp, url_prefix='/battles')

    return app

if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument(
        "-p", "--port", default=5000, type=int, help="port to listen on"
    )
    args = parser.parse_args()
    port = args.port

    app = create_app()

    app.run(host="0.0.0.0", port=port)
