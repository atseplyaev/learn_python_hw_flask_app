from flask import Blueprint, render_template
from flask_login import current_user
from webapp.user.decorators import admin_required
bp = Blueprint("admin", __name__, url_prefix="/admin")


@bp.route("/")
@admin_required
def admin_index():
    title = "Панель администратора"
    return render_template("admin/index.html", page_title=title)

