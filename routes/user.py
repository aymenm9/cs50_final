from flask import Flask, render_template, request, redirect, session, url_for, Blueprint
from cs50_final import DB
from werkzeug.security import generate_password_hash

user_bp = Blueprint("user", __name__, url_prefix="/")


@user_bp.route("/singup", methods=["GET", "POST"])
def singup():

    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")
        
        if not username or not password:
            return render_template("singup.html", error="All fields are required")

        if DB.execute("SELECT * FROM users WHERE username = ?", username):
            return render_template("singup.html", error="User already exists")

        DB.execute("INSERT INTO users (username, hash) VALUES(?, ?)", username, generate_password_hash(password))
        return redirect(url_for("user.login"))
    
    users = DB.execute("SELECT * FROM users")
    return 'singup'