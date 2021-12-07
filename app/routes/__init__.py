from flask import Flask


def init_app(app: Flask):

    from .parameters_routes import bp as bp_parameters
    app.register_blueprint(bp_parameters) 
    
    ...
