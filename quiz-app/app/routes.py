from flask import render_template, send_from_directory
from app import app
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

@app.route("/")
def index():
    return render_template("main.html")

@app.route("/quiz")
def quiz():
    return render_template("quiz.html")

@app.route("/end")
def end():
    return render_template("end.html")

@app.route("/review")
def review():
    return render_template("review.html")

@app.route("/questions.json")
def questions():
    return send_from_directory(os.path.join(BASE_DIR, "static"), "questions.json")