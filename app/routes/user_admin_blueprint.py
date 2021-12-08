from flask import Blueprint

from app.controllers.user_admin_controller import create_user_admin, create_user_analyst

bp_user_admin = Blueprint("bp_user_admin", __name__)

bp_user_admin.post('/signup')(create_user_admin)
bp_user_admin.post('/admin/new_analyst')(create_user_analyst)