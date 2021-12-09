from flask import Flask


def init_app(app: Flask):
    # BLUEPRINT USERS:
    
    from app.routes.user_blueprint import bp_user
    from app.routes.login_blueprint import bp_login
    app.register_blueprint(bp_user)
    app.register_blueprint(bp_login)
    
    # BLUEPRINT ANALYSIS:

    # BLUEPRINT CLASSES:
    from app.routes.classes_blueprint import bp_classes
    app.register_blueprint(bp_classes)

    # BLUEPRINT PARAMETERS:
    from app.routes.parameters_blueprint import bp_parameters
    app.register_blueprint(bp_parameters)
    
    
    # BLUEPRINT TYPES:
    from app.routes.types_blueprint import bp_types
    app.register_blueprint(bp_types)

    ...
