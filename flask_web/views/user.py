import re
import time
from flask import request, jsonify, make_response, Response
from flask.views import MethodView
from flask_web.models.user_model import User, CookieAuth
from flask_web.config.config import parameter
from flask_web.views.tools import encryption, login_auth, set_jwt

from flask_web import app, Blueprint, db

user_views = Blueprint("user", __name__)


class Test(MethodView):
    """测试用"""

    def get(self):
        return jsonify({"success": 200})


class LoginView(MethodView):
    """ 登陆函数

    """
    decorators = [login_auth]

    def get(self):
        # login_cookie = request.cookies.get("login")
        date = {
            "code": 200
        }
        return jsonify(date)

    def post(self):
        # response = make_response()
        try:
            form = request.form
            user_id = form.get("userid")
            user_pwd = form.get("password")
            current_user = User.query.filter_by(username=user_id).first()
        except Exception as e:
            app.logger.error(e)
            return jsonify({"error": parameter["not_user"]})
        # if encryption(user_pwd) != current_user.password:
        if user_pwd != current_user.password:
            return jsonify({"error": parameter['not_pwd']})
        jwt_dict = {
            "iat": time.time(),
            'id': current_user.username
        }
        for i in CookieAuth.query.filter_by(username=user_id).all():
            db.session.delete(i)
        db.session.commit()

        jw = CookieAuth(username=user_id, cookie=set_jwt(jwt_dict))
        db.session.add(jw)
        db.session.commit()
        ret = {
            "code": 200,
            "success": parameter["login_success"],
            "cookie": set_jwt(jwt_dict)
        }
        return jsonify(ret)


class RegisteView(MethodView):
    """注册接口
    """

    def post(self):
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
                return jsonify({"success": "当前用户已被占用", "code": 400})
            re_name = re.match(r'(\s|\d|_)*', name).string
            if not re_name:
                re_name = re_username
            if re_eamil == email and \
                    re_username == username and \
                    re_name == name and \
                    re_userpassword == userpassword \
                    and re_phone == phone:
                if not User.query.filter_by(username=username).first():
                    try:
                        user = User(username=username, password=userpassword, email=email, phone=phone, name=name)
                        db.session.add(user)
                        db.session.commit()
                    except Exception as e:
                        app.logger.error(e)
                    return jsonify({"success": parameter['create_user_success'], "code": 200})
        return jsonify({"error": parameter['create_user_error']}, 404)
