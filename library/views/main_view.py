from models import libraryBook
from flask import Blueprint, render_template, request
from math import ceil

bp = Blueprint("home", __name__, url_prefix="/")


@bp.route("/")
def home():
    page = request.args.get("page", 1)
    page = int(page)
    page_size = 8
    limit = page * page_size
    offset = limit - page_size
    page_count = ceil(libraryBook.query.count() / page_size)
    books = libraryBook.query.order_by(libraryBook.id.asc())[offset:limit]
    page_range = range(1, page_count + 1)
    return render_template(
        "index.html",
        page=page,
        books=books,
        page_count=page_count,
        page_range=page_range,
    )
