from flask import Flask, render_template, send_from_directory

app = Flask(__name__, static_folder="static", template_folder="templates")


# kezdőlap
@app.route("/")
def index():
    return render_template("main.html")


# kérdések oldal
@app.route("/quiz")
def quiz():
    return render_template("quiz.html")


# végeredmény oldal
@app.route("/end")
def end():
    return render_template("end.html")


# kérdések JSON kiszolgálása
@app.route("/questions.json")
def questions():
    return send_from_directory("static", "questions.json")


if __name__ == "__main__":
    app.run(debug=True)
