from datetime import date
from models import libraryBook, rentalBook, bookComment, db
from flask import Blueprint, redirect, render_template, request, url_for
from math import ceil

bp = Blueprint("home", __name__, url_prefix="/")


def avg_rating(book_id):
    all_rating = bookComment.query.filter(bookComment.book_id == book_id).all()
    sum_rating = 0
    if len(all_rating) > 0:
        for rate in all_rating:
            sum_rating += rate.rating
        return round(sum_rating / len(all_rating))
    return 0


@bp.route("/")
def home():
    page = request.args.get("page", 1)
    search = request.args.get("search", "")
    searchquery = f"search={search}&" if search else ""
    try:
        page = int(page)
    except ValueError:
        return redirect(url_for("index"))

    page_size = 8
    limit = page * page_size
    offset = limit - page_size

    books = libraryBook.query.filter(
        libraryBook.book_name.like(f"%{search}%")
    ).order_by(libraryBook.id.asc())

    book_count = books.count()
    page_count = ceil(book_count / page_size)
    books = books[offset:limit]

    for book in books:
        libBook = libraryBook.query.filter(libraryBook.id == book.id).first()
        borBook = (
            rentalBook.query.filter(rentalBook.book_id == book.id)
            .order_by(rentalBook.rental_date.desc())
            .first()
        )
        try:
            if borBook.return_date <= date.today():
                libBook.rented = False
        except AttributeError:
            continue
        else:
            db.session.commit()

    page_range = range(1, page_count + 1)

    if page < 1 or page > page_count:
        return redirect(url_for("index"))

    return render_template(
        "index.html",
        page=page,
        books=books,
        book_count=book_count,
        page_count=page_count,
        page_range=page_range,
        avg_rating=avg_rating,
        search=search,
        searchquery=searchquery,
    )
