from flask import Blueprint

from app.controllers.user_controller import create_user_admin, create_user_analyst

bp_user = Blueprint("bp_user_admin", __name__)

bp_user.post('/signup')(create_user_admin)
bp_user.post('/admin/new_analyst')(create_user_analyst)