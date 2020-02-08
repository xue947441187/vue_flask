# coding:utf-8
from flask import Flask, session, make_response, request, Blueprint, Response, jsonify
from flask_web import config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import *
import logging

app = Flask(__name__)
CORS(app)
app.config.from_object("flask_web.config.config")
handler = logging.FileHandler("..\logs\\all.log")
app.logger.addHandler(handler)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from flask_web.models import user_model
from flask_web.views.user import user_views
app.register_blueprint(user_views)