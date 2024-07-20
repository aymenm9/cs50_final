from flask import Flask, render_template, request, redirect, session, url_for, Blueprint
from project import db, login_user, login_required, singup_user, htmx_required
from werkzeug.security import generate_password_hash, check_password_hash

user_bp = Blueprint("user", __name__, url_prefix="/")


@user_bp.route("/singup", methods=["GET", "POST"])
@htmx_required
def singup():

    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")
        email = request.form.get("email")

        error = singup_user(username, email, password)
        if not error['error']:
            return redirect (url_for("home.home"))

        return render_template("singup.html", error=error)


    return render_template("singup.html")


@user_bp.route("/login", methods=["GET", "POST"])
@htmx_required
def login():

    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")

        error = login_user(username, password)
        if not error['error']:
            return redirect(url_for("home.home"))

        return render_template("login.html", error=error)

    return render_template("login.html")


@user_bp.route("/logout", methods=["POST"])
@login_required
def logout():
    session.clear()
    return redirect(url_for("home.home"))