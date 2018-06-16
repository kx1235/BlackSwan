from flask import Flask, render_template, request
from api_handler import data_getter


app = Flask(__name__)
data_getter.request_access()


@app.route('/')
def index():
    return render_template("home.html", controller=data_getter)


@app.route('/get_code', methods=['POST'])
def get_code():
    """Get the code from the form when requesting access, then finish authentication"""
    return render_template("home.html", controller=data_getter)


@app.route('/get_data', methods=['POST'])
def get_data():
    """Page for getting data from endpoints"""
    endpoint = request.form['endpoint']
    data_getter.get_data(endpoint)
    return render_template("home.html", controller=data_getter)


@app.route('/auth')
def auth():
    """Get the authorization code from URL"""
    code = request.args.get('code')
    data_getter.credentials['code'] = code
    data_getter.token_exchange()
    data_getter.get_first_name()  # TODO: Remove this
    # return render_template("auth.html", controller=data_getter, code=code)  Auth page
    return render_template("home.html", controller=data_getter)


if __name__ == "__main__":
    app.run(host='localhost', debug=True, port=3000)

