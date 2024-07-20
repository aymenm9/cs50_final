from werkzeug.security import generate_password_hash, check_password_hash
from flask import session, redirect, render_template, request, url_for
from .db import db
from functools import wraps

def singup(username, email, password):

    error = {
        'error' : False, 'username' : False, 'password' : False, 'email' : False
    }

    if not username or not password or not email:
        error['error'] = True
        error['username'] = True
        error['password'] = True
        error['email'] = True
        return error

    if db.execute("SELECT * FROM users WHERE username = ?", username):
        error['error'] = True
        error['username'] = True
        return error

    db.execute("INSERT INTO users (username, email, hash) VALUES(?, ?, ?)", username, email, generate_password_hash(password))
    return error 

def login(username, password):

    error = {
        'error' : False, 'username' : False, 'password' : False
    }

    if not username or not password:
        error['error'] = True
        error['username'] = True
        error['password'] = True
        return error

    user = db.execute("SELECT * FROM users WHERE username = ?", username)[0]

    if not user:
        error['error'] = True
        error['username'] = True
        return error
    if not check_password_hash(user["hash"], password):
        error['error'] = True
        error['password'] = True
        return error
    else :
        session["user_id"] = user["id"]
        return error
    
def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not session.get("user_id"):
            return render_template("login.html")
        return func(*args, **kwargs)
    return wrapper

def htmx_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not request.headers.get("HX-Request"):
            return redirect(url_for("index"))
        return func(*args, **kwargs)
    return wrapper