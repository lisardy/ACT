import flask
from flask import render_template, redirect, url_for

app = flask.Flask(__name__, static_url_path='', static_folder='static', template_folder='template')
app.config["DEBUG"] = True

"""
Start the flask app

:returns: None
"""
def run():
    app.run(host="localhost", port=8080, debug=True)


@app.route("/")
def home():
    return render_template("index.html")
