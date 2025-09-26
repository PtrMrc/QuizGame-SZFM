from flask import Flask, render_template, send_from_directory

def create_app():
    app = Flask(__name__, static_folder="static", template_folder="templates")

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
        return send_from_directory("static", "questions.json")

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
