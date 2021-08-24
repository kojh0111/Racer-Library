import os
from flask import Flask, render_template
from flask_migrate import Migrate
from db_connect import db
import config
import dotenv
from flask_restful import Api

migrate = Migrate()


def create_app():
    app = Flask(__name__)
    api = Api(app)
    app.secret_key = os.environ.get("SECRET_KEY")
    app.config.from_object(config)

    db.init_app(app)
    migrate.init_app(app, db)

    from views import main_view, auth_view, book_view

    api.add_resource(auth_view.Register, "/register")

    app.register_blueprint(main_view.bp)
    app.register_blueprint(auth_view.bp)
    app.register_blueprint(book_view.bp)
    app.add_url_rule("/", endpoint="index")

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template("404.html"), 404

    return app


if __name__ == "__main__":
    dotenv.read_dotenv()
    create_app().run(debug=True)
