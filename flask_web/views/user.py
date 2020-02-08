import time

from flask import request, jsonify, make_response
from flask.views import MethodView
from flask_web.models.user_model import User
from flask_web.config.config import parameter
from flask_web.views.tools import encryption, login_auth, get_jwt

from flask_web import app, Blueprint

user_views = Blueprint("user", __name__)


class Test(MethodView):
    """测试用"""

    def get(self):
        return make_response({"success": 200})


class LoginView(MethodView):
    """
    登陆函数
    """
    decorators = [login_auth]

    def get(self):
        response = make_response()
        date = {
            "success": 200
        }
        return response(date)

    def post(self):
        response = make_response()
        try:
            form = request.form
            user_id = form.get("userid")
            user_pwd = form.get("password")
            current_user = User.query.filter_by(user_id=user_id).first()
        except Exception as e:
            app.logger.error(e)
            return response({"error": parameter["not_user"]})
        if encryption(user_pwd) != current_user.password:
            return response({"error": parameter['not_pwd']})
        jwt_dict = {
            "iat": time.time(),
            'id': current_user.user_id
        }
        ret = {
            "success": parameter["login_success"],
            "cookie": get_jwt(jwt_dict)
        }
        return response(ret)


class RegisteView(MethodView):
    def post(self):
        pass
