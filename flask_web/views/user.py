import re
import time

from flask import request, jsonify, make_response, Response
from flask.views import MethodView
from flask_web.models.user_model import User
from flask_web.config.config import parameter
from flask_web.views.tools import encryption, login_auth, get_jwt

from flask_web import app, Blueprint, db

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
            return jsonify({"error": parameter["not_user"]})
        if encryption(user_pwd) != current_user.password:
            return jsonify({"error": parameter['not_pwd']})
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
        # response = Response()
        # response.headers["Access-Control-Allow-Origin"] = "*"
        # response.headers["Access-Control-Allow-Methods"] = "POST"
        # response.headers["Access-Control-Allow-Headers"] = "x-requested-with"

        # request.headers.get("Access-Control-Allow-Origin","*")
        if request.method == 'POST':
            try:
                # response.headers('Access-Control-Allow-Origin','*')
                post = request.form
                username = post['username']
                userpassword = post['userpwd']
                email = post['eamil']
                phone = post['phone']
                name = post['name']

                re_eamil = re.match(r".*\@(163|qq)\.com", email).string
                re_username = re.match(r'(\s|\d|_){6,}', username).string
                re_userpassword = re.match(r'^\w+$', userpassword).string

                re_phone = re.match(r'^1[3|4|5|8][0-9]\d{4,8}$', phone).string
            except Exception as e:
                return jsonify({"error": e})
            try:
                user = User.query.filter_by(username=username).first()
            except Exception as e:
                user = False
            if user:
                return jsonify({"success": "当前用户已被占用"}, 404)
            re_name = re.match(r'(\s|\d|_)*', name).string
            if not re_name:
                re_name = re_username
            if re_eamil == email and \
                    re_username == username and \
                    re_name == name and \
                    re_userpassword == userpassword \
                    and re_phone == phone:
                if not User.query.filter_by(username=username).first():
                    user = User(username=username, passwrod=userpassword, email=email, phone=phone, name=name)
                    db.session.add(user)
                    db.session.commit()
                    return jsonify({"success": parameter['create_user_success']},200)
        return jsonify({"error": parameter['create_user_error']}, 404)
