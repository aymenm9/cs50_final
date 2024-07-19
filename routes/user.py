from flask import Flask, render_template, request, redirect, session, url_for, Blueprint
from cs50 import db
user = Blueprint("user", __name__, url_prefix="/")


@user.route("/singup", methods=["GET", "POST"])
def singup():

    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")
        
        if not username or not password:
            return render_template("singup.html", error="All fields are required")
        
        db
    return render_template("singup.html")