from db_connect import db
from datetime import date, timedelta


class libraryUser(db.Model):

    __tablename__ = "user"

    username = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(100), primary_key=True)
    password = db.Column(db.String(100), nullable=False)
    borrow_book = db.Column(db.String(100), nullable=True)

    def __init__(self, email, password, username):
        self.email = email
        self.password = password
        self.username = username


class libraryBook(db.Model):

    __tablename__ = "book"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    book_name = db.Column(db.String(200))
    publisher = db.Column(db.String(100))
    author = db.Column(db.String(20))
    publication_date = db.Column(db.Date)
    pages = db.Column(db.String(4))
    isbn = db.Column(db.String(13))
    description = db.Column(db.Text())
    link = db.Column(db.String(255))
    photo = db.Column(db.String(255))
    rented = db.Column(db.Boolean, default=False)


class rentalBook(db.Model):

    __tablename__ = "rentalBook"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    book_id = db.Column(
        db.Integer, db.ForeignKey("book.id", ondelete="CASCADE"), nullable=False
    )
    user_id = db.Column(
        db.String(100), db.ForeignKey("user.email", ondelete="CASCADE"), nullable=False
    )
    rental_date = db.Column(db.Date, default=date.today())
    return_date = db.Column(db.Date, default=date.today() + timedelta(days=7))


class bookComment(db.Model):

    __tablename__ = "comment"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    book_id = db.Column(
        db.Integer, db.ForeignKey("book.id", ondelete="CASCADE"), nullable=False
    )
    user_id = db.Column(
        db.String(100), db.ForeignKey("user.email", ondelete="CASCADE"), nullable=False
    )
    rating = db.Column(db.Integer, nullable=False)
    content = db.Column(db.Text(), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)

    def __init__(self, rating, content):
        self.rating = rating
        self.content = content
