from flask import Blueprint, render_template
from flask_login import current_user
from webapp.user.decorators import admin_required
bp = Blueprint("admin", __name__, url_prefix="/admin")


@bp.route("/")
@admin_required
def admin_index():
    if current_user.is_admin:
        return "Привет админ"

    return "Ты не админ"
