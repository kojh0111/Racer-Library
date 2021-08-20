from models import libraryUser, db
from flask import (
    Blueprint,
    render_template,
    redirect,
    url_for,
    request,
    session,
    flash,
    g,
)
from werkzeug.security import generate_password_hash, check_password_hash
from validator import passwordCheck, emailCheck, usernameCheck
import functools

bp = Blueprint("auth", __name__, url_prefix="/auth")


@bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        user = libraryUser.query.filter(libraryUser.email == email).first()
        if not (email and password):
            errormsg = "빈 칸이 있습니다. 모두 입력해주세요."
            return render_template(
                "auth/login.html",
                errormsg=errormsg,
                email=email,
                password=password,
            )

        if not emailCheck(email):
            errormsg = "이메일 형식이 아닙니다."
            return render_template(
                "auth/login.html",
                errormsg=errormsg,
                email=email,
                password=password,
            )
        elif len(password) < 8:
            errormsg = "비밀번호가 너무 짧습니다. 다시 확인해주세요."
            return render_template(
                "auth/login.html",
                errormsg=errormsg,
                email=email,
                password=password,
            )

        if not user:
            errormsg = "아이디 또는 비밀번호가 틀립니다. 다시 한 번 확인해주세요."
            return render_template(
                "auth/login.html",
                errormsg=errormsg,
                email=email,
                password=password,
            )
        elif not check_password_hash(user.password, password):
            errormsg = "비밀번호가 일치하지 않습니다."
            return render_template(
                "auth/login.html",
                errormsg=errormsg,
                email=email,
                password=password,
            )

        session.clear()
        session["username"] = user.username
        session["email"] = user.email
        return redirect(url_for("index"))

    if g.user:
        flash("잘못된 접근입니다.")
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
            errormsg = "이미 존재하는 아이디 입니다."
            return render_template(
                "auth/register.html",
                errormsg=errormsg,
                username=username,
                email=email,
                password=password,
                password2=password2,
            )
        elif password != password2:
            errormsg = "비밀번호가 일치하지 않습니다."
            return render_template(
                "auth/register.html",
                errormsg=errormsg,
                username=username,
                email=email,
                password=password,
                password2=password2,
            )
        else:
            # 정규표현식으로 체크하기!
            if (
                usernameCheck(username)
                and emailCheck(email)
                and passwordCheck(password)
            ):
                password = generate_password_hash(password)
                user = libraryUser(email=email, password=password, username=username)
                db.session.add(user)
                db.session.commit()

                session.clear()
                session["username"] = user.username
                session["email"] = user.email
                return redirect(url_for("index"))
            else:
                errormsg = "유효하지 않는 값이 존재합니다."
                return render_template(
                    "auth/register.html",
                    errormsg=errormsg,
                    username=username,
                    email=email,
                    password=password,
                    password2=password2,
                )

    if g.user:
        flash("잘못된 접근입니다.")
        return redirect(url_for("index"))

    return render_template("auth/register.html")


@bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))


@bp.before_app_request
def load_logged_in_user():
    user_id = session.get("email")
    if user_id:
        g.user = libraryUser.query.filter(libraryUser.email == user_id).first()
    else:
        g.user = None


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for("index"))
        return view(**kwargs)

    return wrapped_view
