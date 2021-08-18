from models import *
from flask import Blueprint, render_template, redirect, url_for, request, session, flash
from werkzeug.security import generate_password_hash, check_password_hash

bp = Blueprint("auth", __name__, url_prefix="/auth")


@bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        user = libraryUser.query.filter(libraryUser.email == email).first()
        if not user:
            return redirect(url_for("auth.login"))
        elif not check_password_hash(user.password, password):
            return redirect(url_for("auth.login"))

        session.clear()
        session["username"] = user.username
        session["email"] = user.email
        return redirect(url_for("index"))

    return render_template("auth/login.html")


@bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]
        password2 = request.form["passwordcheck"]
        user = libraryUser.query.filter(libraryUser.email == email).first()
        if user:
            flash("이미 존재하는 아이디 입니다.")
            return redirect(url_for("auth.register"))
        elif password != password2:
            flash("비밀번호가 일치하지 않습니다.")
            return redirect(url_for("auth.register"))
        else:
            password = generate_password_hash(password)
            user = libraryUser(email=email, password=password, username=username)
            db.session.add(user)
            db.session.commit()

            session.clear()
            session["username"] = user.username
            session["email"] = user.email
            return redirect("index")

    return render_template("auth/register.html")


@bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))
