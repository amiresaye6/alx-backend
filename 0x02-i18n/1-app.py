#!/usr/bin/env python3
"""
task: 1. Basic Babel setup
condition: mandatory
required:

Install the Babel Flask extension:

$ pip3 install flask_babel==2.0.0
Then instantiate the Babel object in your app. Store it in a module-level
variable named babel.

In order to configure available languages in our app, you will create a Config
class that has a LANGUAGES class attribute equal to ["en", "fr"].

Use Config to set Babel’s default locale ("en") and timezone ("UTC").

Use that class as config for your Flask app.
"""
from flask_babel import Babel
from flask import Flask, render_template


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


@app.route('/')
def get_index() -> str:
    """The home/index page.
    """
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
