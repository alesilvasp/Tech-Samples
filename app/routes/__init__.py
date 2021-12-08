from flask import Flask
from app.routes.user_admin_blueprint import bp_user_admin
from app.routes.login_blueprint import bp_login


def init_app(app: Flask):

    app.register_blueprint(bp_user_admin)
    app.register_blueprint(bp_login)
