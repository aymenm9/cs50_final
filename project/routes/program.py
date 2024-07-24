from flask import Flask, render_template, request, redirect, session, url_for, Blueprint
from project import db, login_required, htmx_required
import uuid

program_bp = Blueprint("program", __name__, url_prefix="/")


@program_bp.route("/addprogram", methods=["POST"])
@htmx_required
@login_required
def addprogram():
    name = request.form.get("program_name")
    description = request.form.get("program_description")
    duration = request.form.get("program_duration")
    db.execute("INSERT INTO programs (name, description, duration, completed, user_id) VALUES(?, ?, ?, ?, ?)", name, description,duration,False, session["user_id"])
    if request.form.get("page") == "home":
        return render_template("success.html", msg = "Program added successfully!")
    elif request.form.get("page") == "program":
        return redirect("/program")

@program_bp.route("/getprograms")
@login_required
@htmx_required
def getprograms():
    programs = db.execute("SELECT * FROM programs WHERE user_id = ?", session["user_id"])
    return render_template("select_programs.html", programs = programs)




@program_bp.route("/addworkout", methods=["POST"])
@htmx_required
@login_required
def addworkout():
    name = request.form.get("workout_name")
    program_id = int(request.form.get("program_id"))
    workout_id = db.execute("INSERT INTO workouts (name, completed , program_id) VALUES(?, ?, ?)", name, False, program_id)
    exercises = request.form.to_dict()
    exercises.pop("workout_name")
    exercises.pop("program_id")
    exercises_name = dict()
    exercises_repetition = dict()
    for key in exercises:
        uid, name = key.split("_")
        if name == 'name':
            exercises_name[uid] = exercises[key]
        else:
            if uid in exercises_name:
                exercise_id = db.execute("INSERT INTO exercises (name, reps, completed, workout_id) VALUES(?, ?, ?, ?)", exercises_name[uid], int(exercises[key]), False, workout_id)

                exercises_name.pop(uid)
            else:
                exercises_repetition[uid] = exercises[key]
    for id in exercises_name:
        db.execute("INSERT INTO exercises (name, reps, completed, workout_id) VALUES(?, ?, ?, ?)", exercises_name[id], int(exercises_repetition[id]), False, workout_id)

    return render_template("success.html", msg = "Workout added successfully!")



@program_bp.route("/addexercise", methods=["GET","POST"])
@htmx_required
@login_required
def addexercise():
    if request.method == "POST":
        ...
    uid = uuid.uuid4().hex
    return render_template("addexercise.html", uid = uid)