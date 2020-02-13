from flask import Blueprint
from flask_login import current_user, login_required
bp = Blueprint("admin", __name__, url_prefix="/admin")


@bp.route("/admin")
@login_required
def admin_index():
    if current_user.is_admin:
        return "Привет админ"

    return "Ты не админ"
