# module 11 - Flask Application
# Mike Colbert 3/31/2026

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/")
def hello():
    return "Hello World!!"


@app.route("/jack")
def jack():
    x = 6
    y = 15
    z = x + y
    name = "Jack"
    return f"Hello {name}, the sum of {x} and {y} is {z}!"


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003, debug=True)
