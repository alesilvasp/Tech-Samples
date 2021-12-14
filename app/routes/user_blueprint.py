from flask import Blueprint

from app.controllers.user_controller import change_password, create_user_admin, create_user_analyst, read_users

bp_user = Blueprint("bp_user_admin", __name__)

bp_user.post('/signup')(create_user_admin)  # Only to create new admin

bp_user.post('/admin/new_analyst')(create_user_analyst)

bp_user.patch('/profile')(change_password)

bp_user.get('/users')(read_users)
