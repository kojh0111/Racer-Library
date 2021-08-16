from flask import Flask
from db_connect import db


def create_app():
    app = Flask(__name__)
    db.init_app(app)

    return app


if __name__ == "__main__":
    create_app().run(debug=True)
