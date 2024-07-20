from flask import Flask, render_template, request, redirect, session, url_for, Blueprint
from project import db
from werkzeug.security import generate_password_hash, check_password_hash

user_bp = Blueprint("user", __name__, url_prefix="/")


@user_bp.route("/singup", methods=["GET", "POST"])
def singup():

    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")
        
        if not username or not password:
            return render_template("singup.html", error="All fields are required")

        if db.execute("SELECT * FROM users WHERE username = ?", username):
            return render_template("singup.html", error="User already exists")

        db.execute("INSERT INTO users (username, hash) VALUES(?, ?)", username, generate_password_hash(password))
        return redirect(url_for("user.login"))

    return render_template("singup.html")


@user_bp.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")

        user = db.execute("SELECT * FROM users WHERE username = ?", username)

        if not user or not check_password_hash(user["hash"], password):
            return render_template("login.html", error="Invalid credentials")

        session["user_id"] = user["id"]
        return redirect(url_for("user.index"))
    return render_template("login.html")


@user_bp.route("/auth")
def auth():
    return render_template("auth.html")