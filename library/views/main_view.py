from datetime import date
from models import libraryBook, rentalBook, db
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
    for book in books:
        libBook = libraryBook.query.filter(libraryBook.id == book.id).first()
        borBook = (
            rentalBook.query.filter(rentalBook.book_id == book.id)
            .order_by(rentalBook.rental_date.desc())
            .first()
        )
        try:
            if borBook.return_date < date.today():
                libBook.rented = False
                db.session.commit()
        except AttributeError:
            continue
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
