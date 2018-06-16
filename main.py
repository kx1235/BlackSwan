from flask import Flask, render_template, request
from api_handler import Controller

app = Flask(__name__)
controller = Controller()
controller.request_access()


@app.route('/')
def index():
    return render_template("home.html", controller=controller)


@app.route('/get_code', methods=['POST'])
def get_code():
    """Get the code from the form when requesting access, then finish authentication
    """
    controller.credentials['code'] = request.form['code']
    controller.token_exchange()
    controller.get_first_name()  # TODO: Remove this
    return render_template("home.html", controller=controller)


@app.route('/get_data', methods=['POST'])
def get_data():
    endpoint = request.form['endpoint']
    controller.get_data(endpoint)
    return render_template("home.html", controller=controller)


if __name__ == "__main__":
    app.run(debug=True, port=3000)
