# coding:utf-8
# sys.path.append(".")
from flask import Flask, session, make_response, request, Blueprint, Response, jsonify
from flask_web import config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_cors import *
import logging
from flask_web.config.config import obj_dir,log

app = Flask(__name__)
CORS(app)
manager = Manager(app)
app.config.from_object("flask_web.config.config")
handler = logging.FileHandler(log)
app.logger.addHandler(handler)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager.add_command('db',MigrateCommand)

from flask_web.models import user_model
from flask_web.views.user import user_views
app.register_blueprint(user_views)
@app.route("/")
def index():
    pass