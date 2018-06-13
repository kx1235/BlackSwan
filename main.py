from flask import Flask, render_template, request
from flask_sslify import SSLify
from api_handler import Controller

# Set up app
app = Flask(__name__)

# Set up controller
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


@app.route('/auth', methods=['GET', 'POST'])
def auth():
    access_token = request.args.get('code')
    print(access_token)
    return render_template("auth.html", access_token=access_token, controller=controller)


if __name__ == "__main__":
    app.run(debug=False, host="localhost", port=3000)
