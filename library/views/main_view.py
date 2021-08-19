from models import libraryBook
from flask import Blueprint, redirect, render_template, request, url_for
from math import ceil

bp = Blueprint("home", __name__, url_prefix="/")


@bp.route("/")
def home():
    page = request.args.get("page", 1)
    try:
        page = int(page)
    except ValueError:
        return redirect(url_for("index"))
    page_size = 8
    limit = page * page_size
    offset = limit - page_size
    page_count = ceil(libraryBook.query.count() / page_size)
    books = libraryBook.query.order_by(libraryBook.id.asc())[offset:limit]
    page_range = range(1, page_count + 1)
    if page < 1 or page > page_count:
        return redirect(url_for("index"))
    return render_template(
        "index.html",
        page=page,
        books=books,
        page_count=page_count,
        page_range=page_range,
    )
