from flask import Flask, render_template, request, redirect, session, url_for, Blueprint
from project import db, login, login_required, singup, htmx_required
from werkzeug.security import generate_password_hash, check_password_hash

user_bp = Blueprint("user", __name__, url_prefix="/")


@user_bp.route("/singup", methods=["GET", "POST"])
@htmx_required
def singup():

    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")


    return render_template("singup.html")


@user_bp.route("/login", methods=["GET", "POST"])
@htmx_required
def login():

    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")

        error = login(username, password)
        if not error['error']:
            return redirect(url_for("user.home"))

        return render_template("login.html", error=error)

    return render_template("login.html")