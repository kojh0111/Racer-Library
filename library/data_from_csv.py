# import click
import csv
from datetime import date

# from flask.cli import with_appcontext
from models import libraryBook, db
from app import create_app

app = create_app()
app.app_context().push()


def init_book_db():
    if libraryBook.query.first() is None:
        with app.app_context():
            with open("./books_src/elice_books.csv", encoding="utf-8") as books:
                reader = csv.DictReader(books)
                for r in reader:
                    book_id = r["book_id"]
                    photo = f"./static/book_img/{book_id}.jpg"
                    book = libraryBook(
                        id=book_id,
                        book_name=r["book_name"],
                        publisher=r["publisher"],
                        author=r["author"],
                        publication_date=date.fromisoformat(r["publication_date"]),
                        pages=r["pages"],
                        isbn=r["isbn"],
                        description=r["description"],
                        link=r["link"],
                        photo=photo,
                    )
                    db.session.add(book)
                    db.session.commit()
            db.create_all(app=app)


init_book_db()
# @click.command("init-book-db")
# @with_appcontext
# def init_book_db_cmd():
#     init_book_db()
#     click.echo("Book DB 추가 완료")


# def init_app(app):
#     app.cli.add_command(init_book_db_cmd)
