from flask.views import MethodView

from flask_web import app
from flask_web.views.tools import login_auth, get_jwt
from flask import jsonify, request
from flask_web.models.user_model import PersonalInfoTable

class LoginInfo(MethodView):
    decorators = [login_auth]

    def get(self):
        user_id = get_jwt(request.cookies.get("login"))["id"]
        date = {}
        try:
            user_info_db = PersonalInfoTable.query.filter_by(name=user_id).first()
        except Exception as e:
            app.logger.error(e)
        if user_info_db is None:
            date["success"] = "registe"
        elif user_info_db is not None:
            date["success"] = {
                "age": user_info_db.age,
                "name":user_info_db.name,
                "sex": user_info_db.sex,
                "height": user_info_db.height,
                "wetght": user_info_db.wetght
            }

        return jsonify(date,200)