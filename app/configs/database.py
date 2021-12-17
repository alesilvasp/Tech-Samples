from operator import imod
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_app(app: Flask):
    db.init_app(app)

    app.db = db

    db.app = app

    from app.models.analysis_model import AnalysisModel
    from app.models.classes_model import ClassModel
    from app.models.parameters_model import ParameterModel
    from app.models.types_model import TypeModel
    from app.models.users_model import UserModel