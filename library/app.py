from flask import Flask
from flask_migrate import Migrate
from db_connect import db
import config

migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)
    migrate.init_app(app, db)

    from views import main_view, auth_view
    import models

    app.register_blueprint(main_view.bp)
    app.register_blueprint(auth_view.bp)
    app.add_url_rule("/", endpoint="index")

    return app


if __name__ == "__main__":
    create_app().run(debug=True)
