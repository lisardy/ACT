import flask
from flask import render_template, redirect, url_for
import data.data_controller as data_controller

app = flask.Flask(__name__, static_url_path='', static_folder='static', template_folder='template')
app.config["DEBUG"] = True

# bad way to do this but oh well
item_interface = data_controller.get_item_interface()
items = item_interface.get_items()
low_probability_count = item_interface.get_low_probability_count()
medium_probability_count = item_interface.get_medium_probability_count()
high_probability_count = item_interface.get_high_probability_count()

"""
Start the flask app

:returns: None
"""
def run():
    app.run(host="localhost", port=8080, debug=True)


@app.route("/")
def show_root():
    return render_template("dashboard.jinja", vulnerabilities=items, low_count=low_probability_count, medium_count=medium_probability_count, high_count=high_probability_count)

@app.route("/dashboard")
def show_dashboard():
    return redirect("/")

@app.route("/vulnerabilities")
def show_vulnerabilities():
    return render_template("vulnerabilities.jinja", vulnerabilities=items)

@app.route("/test")
def show_test():
    return render_template("test.html")
