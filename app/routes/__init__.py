from flask import Flask


def init_app(app: Flask):
    # BLUEPRINT USERS:

    # from app.routes.user_admin_blueprint import bp_user_admin
    # from app.routes.login_blueprint import bp_login
    # app.register_blueprint(bp_user_admin)
    # app.register_blueprint(bp_login)

    # BLUEPRINT ANALYSIS:

    # BLUEPRINT CLASSES:
    from app.routes.classes_blueprint import bp_classes
    app.register_blueprint(bp_classes)

    # BLUEPRINT PARAMETERS:

    # BLUEPRINT TYPES:

    ...
