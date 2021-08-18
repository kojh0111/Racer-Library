from models import libraryBook
from flask import Blueprint, render_template

bp = Blueprint("book", __name__, url_prefix="/book")


@bp.route("/<int:book_id>")
def book_detail(book_id):
    book = libraryBook.query.filter(libraryBook.id == book_id).first()
    return render_template("services/detail.html", book=book)
