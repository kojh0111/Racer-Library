from faker import Faker
from random import randint
from datetime import timedelta

from models import bookComment, db

from app import create_app

app = create_app()
app.app_context().push()

emails = [
    "coejimin@naver.com",
    "donghyeon39@gmail.com",
    "egim@live.com",
    "ejin@nate.com",
    "eungyeong23@nate.com",
    "gimjungsu@live.com",
    "hayuncoe@dreamwiz.com",
    "hgwag@nate.com",
    "hgweon@hotmail.com",
    "hyeonjeongjang@hanmail.net",
    "igwangsu@daum.net",
    "ihyejin@nate.com",
    "iseojun@hanmail.net",
    "iyujin@naver.com",
    "janghaeun@dreamwiz.com",
    "jeongsug63@dreamwiz.com",
    "jeongsug85@gmail.com",
    "jeongunggwag@hotmail.com",
    "jgwag@hotmail.com",
    "jihyeon09@nate.com",
    "jihyeon94@hotmail.com",
    "junhyeogu@hotmail.com",
    "mbag@nate.com",
    "minjunjeong@dreamwiz.com",
    "minseo25@hotmail.com",
    "myeongjai@dreamwiz.com",
    "namjaeho@hotmail.com",
    "namjeongung@nate.com",
    "ngim@gmail.com",
    "ohan@dreamwiz.com",
    "pi@hanmail.net",
    "rgim@dreamwiz.com",
    "seojun54@hotmail.com",
    "seongsu39@gmail.com",
    "seongyeongsug@live.com",
    "sunognam@live.com",
    "test@te.st",
    "ui@daum.net",
    "yeonghohan@gmail.com",
    "yeongjin12@dreamwiz.com",
    "ygim@live.com",
]
fake = Faker(["ko_KR"])

for _ in range(1000):
    email = fake.word(ext_word_list=emails)
    rating = randint(1, 5)
    book_id = randint(1, 32)
    content = fake.paragraph(nb_sentences=3)
    micro = randint(0, 999999)
    created_at = fake.date_time_between(start_date="-60d") - timedelta(
        microseconds=micro
    )
    print(f"{email=} {book_id=} {content=} {rating=} {created_at=}")
    comment = bookComment(
        user_id=email,
        book_id=book_id,
        content=content,
        rating=rating,
        created_at=created_at,
    )
    db.session.add(comment)

db.session.commit()
