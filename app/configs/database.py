from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_app(app: Flask):
    db.init_app(app)

    app.db = db

    from app.models.analisys_model import AnalisysModel
    from app.models.classes_model import ClassModel
    from app.models.parameters_model import ParameterModel
    from app.models.types_model import TypeModel
    from app.models.user_admin_model import UserAdminModel
    from app.models.user_analist_model import UserAnalistModel