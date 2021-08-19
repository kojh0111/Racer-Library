from datetime import date
from models import libraryBook, rentalBook, db
from flask import Blueprint, render_template, redirect, url_for, session, flash
from sqlalchemy import and_

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
        db.session.commit()
    else:
        flash("남은 책이 없습니다.")
        book = rentalBook.query.filter(book_id == book_id).first()
    print(type(book.rental_date))
    return redirect(url_for("index"))


@bp.route("/lent")
def book_lent():
    books = rentalBook.query.filter(
        and_(
            rentalBook.user_id == session["email"],
            rentalBook.return_date <= date.today(),
        )
    ).all()
    return render_template("services/lent.html", books=books)


@bp.route("/return")
def book_return():
    books = rentalBook.query.filter(
        and_(
            rentalBook.user_id == session["email"],
            rentalBook.return_date >= date.today(),
        )
    ).all()
    return render_template("services/return.html", books=books)
