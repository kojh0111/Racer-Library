from flask import Blueprint, render_template, redirect, url_for

bp = Blueprint("auth", __name__, url_prefix="/auth")


@bp.route("/login")
def login():
    return render_template("auth/login.html")


@bp.route("/register")
def register():
    return render_template("auth/register.html")


@bp.route("/logout")
def logout():
    # session.clear()
    return redirect(url_for("index"))
