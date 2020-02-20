import hashlib
from flask import request, jsonify
import jwt
from flask_web.config.config import jwt_crt
from flask_web.models.user_model import CookieAuth


def encryption(date):
    """
    :param date: 需要加密的数据
    :return: 加密后的数据
    """
    ret = hashlib.md5("947441187@qq.com".encode('utf-8'))
    ret.update(date.encode("utf-8"))
    retsult = ret.hexdigest()
    return retsult


def get_jwt(date):
    """jwt加密
    :param date: 需要传递的参数
    :return: 加密后的数据
    """
    headers = {
        "alg": "HS256"
    }
    jwt_token = jwt.encode(date,
                           jwt_crt,
                           algorithm='HS256',
                           headers=headers,
                           ).decode('ascii')
    return jwt_token


def set_jwt(date):
    """ jwt解密

    :param date:加密的jwt数据
    :return: 解密后的数据
    """
    jwt_date = jwt.decode(date, jwt_crt, algorithms=["HS256"])
    return jwt_date


def login_auth(func):
    """装饰器效果,判断访问模式,查看参数cookie是否存在,
    post访问如果存在参数则将访问模式改为GET
    :param func:
    :return:
    """

    def sign_auth(*args, **kwargs):
        if request.method == "GET":
            """"""
            try:
                user_id = set_jwt(request.cookies.get("login")).id
                cookie = CookieAuth.query.filter_by(cookie=request.cookies.get("login"))
                db_user_id = set_jwt(cookie).id
            except:
                return jsonify({"code": 405, "success": "登陆信息不对,请返回返回登陆页面"})
            if user_id != db_user_id:
                return jsonify({"code": 405, "success": "登陆信息不对,请返回返回登陆页面"})
            return func(*args, **kwargs)

        if request.method == "POST":
            # return "post 通过"
            try:
                request.cookies.get("login")
            except:
                return func(*args, **kwargs)
            return func(*args, **kwargs)
        return func(*args, **kwargs)

    return sign_auth
