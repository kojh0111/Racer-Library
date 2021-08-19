from models import libraryBook, rentalBook, db
from flask import Blueprint, render_template, redirect, url_for, session, flash

bp = Blueprint("book", __name__, url_prefix="/book")


@bp.route("/<int:book_id>")
def book_detail(book_id):
    book = libraryBook.query.filter(libraryBook.id == book_id).first()
    return render_template("services/detail.html", book=book)


@bp.route("/<int:book_id>/borrow", methods=["POST"])
def borrow_book(book_id):
    libBook = libraryBook.query.filter(libraryBook.id == book_id).first()
    if not libBook.rented:
        libBook.rented = True
        book = rentalBook(book_id=book_id, user_id=session["email"])
        db.session.add(book)
    else:
        flash("남은 책이 없습니다.")
        db.session.commit()
    return redirect(url_for("index"))


@bp.route("/lent")
def book_lent():
    return render_template("services/lent.html")


@bp.route("/return")
def book_return():
    return render_template("services/return.html")
