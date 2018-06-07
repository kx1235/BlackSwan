from flask import Flask, render_template
from api_handler import Controller

app = Flask(__name__)
controller = Controller()


@app.route('/')
def index():
    return render_template("home.html", controller=controller)


if __name__ == "__main__":
    app.run(debug=True)
