from flask import Flask
from webapp.db import db
from webapp.user.models import User

from webapp.user.views import bp as user_bp
from webapp.news.views import bp as news_bp
from webapp.admin.views import bp as admin_bp

from flask_login import LoginManager
from flask_migrate import Migrate

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile("config.py")
    app._static_folder = "templates/static"
    db.init_app(app)
    migrate = Migrate(app, db)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = "user.login"

    app.register_blueprint(user_bp)
    app.register_blueprint(news_bp)
    app.register_blueprint(admin_bp)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
