from flask_web import app
from flask_web.views.user import LoginView, RegisteView,Test
from flask_web.views.userInfo import LoginInfo

# 增加类视图路由
app.add_url_rule("/api/login", view_func=LoginView.as_view("LoginView"))
app.add_url_rule("/api/registe", view_func=RegisteView.as_view("RegisteView"))
app.add_url_rule("/api/test", view_func=Test.as_view("Test"))
app.add_url_rule("/api/logininfo",view_func=LoginInfo.as_view("LoginInfo"))
