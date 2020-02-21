from flask.views import MethodView
from flask_web.views.tools import login_auth
from flask import jsonify


class LoginInfo(MethodView):
    decorators = [login_auth]

    def get(self):
        date = {"success": "详细信息页面"}
        return jsonify(date, 200)
