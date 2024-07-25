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

@program_bp.route("/getprogram")
@login_required
@htmx_required
def getprogram():
    id = int(request.args.get("id"))
    program = db.execute("SELECT * FROM programs WHERE id = ?", id)[0]
    workouts = db.execute("SELECT * FROM workouts WHERE program_id = ?", program["id"])
    return render_template("program.html", program = program, workouts = workouts)


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
    page = request.form.get("page") 
    name = request.form.get("workout_name")
    program_id = int(request.form.get("program_id"))
    workout_id = db.execute("INSERT INTO workouts (name, completed , program_id) VALUES(?, ?, ?)", name, False, program_id)
    exercises = request.form.to_dict()
    exercises.pop("workout_name")
    exercises.pop("program_id")
    exercises.pop("page")
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

    if page == "workout":
        return redirect("/workout")
    return render_template("success.html", msg = "Workout added successfully!")

@program_bp.route("/getworkout")
@login_required
@htmx_required
def getworkouts():
    workout_id = int (request.args.get("id"))
    workout = db.execute("SELECT * FROM workouts WHERE id = ?", workout_id)[0]
    exercises = db.execute("SELECT * FROM exercises WHERE workout_id = ?", workout_id)

    return render_template("workout.html", workout = workout, exercises = exercises)



@program_bp.route("/addexercise", methods=["GET","POST"])
@htmx_required
@login_required
def addexercise():
    if request.method == "POST":
        ...
    uid = uuid.uuid4().hex
    return render_template("addexercise.html", uid = uid)


@program_bp.route("/done")
@htmx_required
@login_required
def done():
    table = request.args.get("table")
    id = int(request.args.get("id"))

    if table not in ["exercises", "workouts", "programs"]:
        return "error"
    
    db.execute("UPDATE ? SET completed = 1 WHERE id = ?",table, id)
    
    if table == "exercises":
        workout_id = db.execute("SELECT workout_id FROM exercises WHERE id = ?", id)[0]["workout_id"]
        return redirect("/getworkout?id=" + str(workout_id))
    elif table == "workouts":
        return redirect("/workout")
    elif table == "programs":
        return redirect("/program")

@program_bp.route("/undone")
@htmx_required
@login_required
def undone():
    table = request.args.get("table")
    id = int(request.args.get("id"))

    if table not in ["exercises", "workouts", "programs"]:
        return "error"
    
    db.execute("UPDATE ? SET completed = 0 WHERE id = ?",table, id)
    
    if table == "exercises":
        workout_id = db.execute("SELECT workout_id FROM exercises WHERE id = ?", id)[0]["workout_id"]
        return redirect("/getworkout?id=" + str(workout_id))
    elif table == "workouts":
        return redirect("/workout")
    elif table == "programs":
        return redirect("/program")