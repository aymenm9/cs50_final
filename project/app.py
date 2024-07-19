from flask import Flask, render_template, request, redirect, session
from flask_session import Session
from .routes import user_bp

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

app.register_blueprint(user_bp)

@app.route("/", methods=["GET", "POST"])
def index():
    return 'hello world!'

if __name__ == "__main__":
    app.run(debug= True)