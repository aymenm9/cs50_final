from flask import Flask, render_template, request, redirect, session, url_for, Blueprint
from project import db, login, login_required
from werkzeug.security import generate_password_hash, check_password_hash


home_bp = Blueprint("home", __name__, url_prefix="/")


@home_bp.route("/home")
@login_required
def home():
    return render_template("home.html")
