import os
from flask import Flask
from flask_migrate import Migrate
from db_connect import db
import config
import dotenv

migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.secret_key = os.environ.get("SECRET_KEY")
    app.config.from_object(config)

    db.init_app(app)
    migrate.init_app(app, db)

    from views import main_view, auth_view

    app.register_blueprint(main_view.bp)
    app.register_blueprint(auth_view.bp)
    app.add_url_rule("/", endpoint="index")

    return app


if __name__ == "__main__":
    dotenv.read_dotenv()
    create_app().run(debug=True)
