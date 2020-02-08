from flask_web import app
from flask_web.views.user import LoginView, RegisteView,Test

# 增加类视图路由
app.add_url_rule("/login/", view_func=LoginView.as_view("LoginView"))
app.add_url_rule("/registe/", view_func=RegisteView.as_view("RegisteView"))
app.add_url_rule("/test/", view_func=Test.as_view("Test"))
