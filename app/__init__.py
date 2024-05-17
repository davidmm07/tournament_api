#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from config import ENV
from flask_migrate import Migrate

# create app
app = Flask(__name__)

if ENV == 'test':
    app.config.from_object('config.ConfigTest')
else:
    app.config.from_object('config.Config')

# create db connection
db = SQLAlchemy(app)
migrate = Migrate(app, db)
ma = Marshmallow(app)

from app.views.monsters import monsters_bp  # noqa: E402
from app.views.battles import battles_bp  # noqa: E402

# register blueprints
app.register_blueprint(monsters_bp, url_prefix='/monsters')
app.register_blueprint(battles_bp, url_prefix='/battles')
