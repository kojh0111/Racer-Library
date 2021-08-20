from datetime import date, datetime
from models import libraryBook, rentalBook, bookComment, db
from flask import Blueprint, render_template, redirect, url_for, session, flash, request
from sqlalchemy import and_
from views.main_view import avg_rating
from views.auth_view import login_required

bp = Blueprint("book", __name__, url_prefix="/book")


@bp.route("/<int:book_id>")
def book_detail(book_id):
    book = libraryBook.query.filter(libraryBook.id == book_id).first()
    comments = (
        bookComment.query.filter(bookComment.book_id == book_id)
        .order_by(bookComment.created_at.desc())
        .all()
    )
    return render_template("services/detail.html", book=book, comments=comments)


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
@login_required
def book_lent():
    books = rentalBook.query.filter(
        and_(
            rentalBook.user_id == session["email"],
            rentalBook.return_date <= date.today(),
        )
    ).all()
    return render_template("services/lent.html", books=books, avg_rating=avg_rating)


@bp.route("/return")
@login_required
def book_return():
    books = rentalBook.query.filter(
        and_(
            rentalBook.user_id == session["email"],
            rentalBook.return_date > date.today(),
        )
    ).all()
    return render_template("services/return.html", books=books, avg_rating=avg_rating)


@bp.route("/<int:book_id>/return", methods=["POST"])
@login_required
def return_book(book_id):
    libBook = libraryBook.query.filter(libraryBook.id == book_id).first()
    if libBook.rented:
        libBook.rented = False
        book = (
            rentalBook.query.filter(rentalBook.book_id == book_id)
            .order_by(rentalBook.rental_date.desc())
            .first()
        )
        book.return_date = date.today()
        db.session.commit()
    else:
        flash("잘못된 접근 입니다.")

    return redirect(url_for("book.book_return"))


@bp.route("/<int:book_id>/comment", methods=["POST"])
@login_required
def comment(book_id):
    rating = request.form["stars"]
    content = request.form["comment"]
    if rating == "0":
        flash("평가하기를 놓치셨군요. 평가하기를 해주세요.")
    elif not content:
        flash("댓글에 내용이 필요합니다.")
    else:
        c = bookComment(
            book_id=book_id,
            user_id=session["email"],
            rating=rating,
            content=content,
            created_at=datetime.utcnow(),
        )
        db.session.add(c)
        db.session.commit()
    return redirect(url_for("book.book_detail", book_id=book_id))
