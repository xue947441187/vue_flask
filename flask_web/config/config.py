# coding:utf-8
import os

DEBUG = True
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'myweb.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_COMMIT_TEARDOWN = True
WTF_CSRF_ENABLED = False

parameter = {
    "create_user_success": "创建用户成功",
    "create_user_error": "创建用户失败 ",
    "signauth_error": "登录认证错错误",
    "login_error": "登录失败确认是否缺少参数",
    "not_user": "此用户不存在",
    "not_pwd": "不存在的密码",
    "login_success": "登陆成功"
}
'''
设置认证
200表示成功
404表示失败

'''
# ------------------------logging------------
FORMAT = '%(asctime)-15s %(clientip)s %(user)-8s %(message)s'

# --------------------jwt-------------
jwt_crt = "@#$!@#$$!#!@$!@!#!@#$!$!@#!#@!!"
