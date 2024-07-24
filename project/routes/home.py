from flask import Flask, render_template, request, redirect, session, url_for, Blueprint
from project import db, login_required, htmx_required
from werkzeug.security import generate_password_hash, check_password_hash


home_bp = Blueprint("home", __name__, url_prefix="/")


@home_bp.route("/home")
@login_required
@htmx_required 
def home():
    return render_template("home.html")


@home_bp.route("/program")
@login_required
@htmx_required
def program():
    programs = db.execute("SELECT * FROM programs WHERE user_id = ?", session["user_id"])
    return render_template("programs.html", programs = programs)


@home_bp.route("/workout")
@login_required
@htmx_required
def workout():
    workouts = db.execute("SELECT * FROM workouts WHERE program_id IN (SELECT id FROM programs WHERE user_id = ?)", session["user_id"])
    for workout in workouts:
        exercises = db.execute("SELECT * FROM exercises WHERE workout_id = ?", workout["id"])
        workout["exercises"] = exercises
        workout["exercises_count"] = len(exercises)
    return render_template("workouts.html", workouts = workouts)

