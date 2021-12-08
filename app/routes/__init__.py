from flask import Flask

def init_app(app: Flask):
    # BLUEPRINT USERS:
    
    from app.routes.user_blueprint import bp_user
    from app.routes.login_blueprint import bp_login
    app.register_blueprint(bp_user)
    app.register_blueprint(bp_login)
    
    # BLUEPRINT ANALYSIS:
    
    
    # BLUEPRINT CLASSES:
    
    
    # BLUEPRINT PARAMETERS:
    
    
    # BLUEPRINT TYPES:
    
    
    ...
