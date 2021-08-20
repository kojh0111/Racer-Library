from faker import Faker
from models import libraryUser, db
from werkzeug.security import generate_password_hash
from app import create_app

app = create_app()
app.app_context().push()

fake = Faker(["ko_KR"])

for _ in range(20):
    email = fake.ascii_free_email()
    password = fake.md5()
    username = fake.name()
    print(f"{email=} {password=} {username=}")
    user = libraryUser(
        username=username, email=email, password=generate_password_hash(password)
    )
    db.session.add(user)

db.session.commit()
