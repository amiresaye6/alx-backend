#!/usr/bin/env python3
"""
task: 2. Get locale from request
condition: mandatory
required:
Create a get_locale function with the babel.localeselector decorator. Use
request.accept_languages to determine the best match with our
supported languages.
"""
from flask import Flask, request, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app, locale_selector="en")


class Config():
    """
    used to set Babel’s default locale ("en") and timezone ("UTC").
    used as config for your Flask app.
    """
    LANGUAGES = ["en", "fr"]


@babel.localeselector
def get_locale():
    """
    determine the best match with our supported languages.
    """


@app.route('/')
def main_page():
    """
    route for an index.html template that simply outputs “Welcome to Holberton”
    as page title (<title>) and “Hello world” as header (<h1>).
    """
    return render_template("0-index.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
