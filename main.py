from flask import render_template, request, redirect

from api_handler import data_getter
import app as app_class
from app import app
from data.data_getter import list_positions

server = app.server
data_getter.request_access()


@server.route('/')
def index():
    return render_template("home.html", controller=data_getter)


@server.route('/get_code', methods=['POST'])
def get_code():
    """Get the code from the form when requesting access, then finish authentication"""
    return render_template("home.html", controller=data_getter)


@server.route('/get_data', methods=['POST'])
def get_data():
    """Page for getting data from endpoints"""
    endpoint = request.form['endpoint']
    data_getter.get_data(endpoint)
    return render_template("home.html", controller=data_getter)


@server.route('/auth')
def auth():
    """Loading screen while data is being downloaded"""
    # Get code WS
    code = request.args.get('code')
    data_getter.credentials['code'] = code

    return render_template("home_loading.html")

@server.route('/load_data')
def load_data():
    """Get the authorization code from URL"""
    # Get authentication token
    data_getter.token_exchange()
    data_getter.get_first_name()  # TODO: Remove this
    # return render_template("auth.html", controller=data_getter, code=code)  # Auth page
    # return render_template("home.html", controller=data_getter)  # Get endpoints page

    # Refresh data somewhere
    app_class.data.update()

    return redirect('/dash')


if __name__ == "__main__":
    server.run(host='localhost', debug=True, port=3000)
