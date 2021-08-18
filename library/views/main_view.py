from models import libraryBook
from flask import Blueprint, render_template

bp = Blueprint("home", __name__, url_prefix="/")


@bp.route("/")
def home():
    books = libraryBook.query.order_by(libraryBook.id.asc())
    return render_template("index.html", books=books)
