#!/usr/bin/env python3
"""
task: 2. Get locale from request
condition: mandatory
required:
Create a get_locale function with the babel.localeselector decorator. Use
request.accept_languages to determine the best match with our
supported languages.
"""
from flask_babel import Babel
from flask import Flask, render_template, request


class Config:
    """Represents a Flask Babel configuration.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """
    etermine the best match with our supported languages
    """

    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def get_index() -> str:
    """The home/index page.
    """
    return render_template('2-index.html')


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
