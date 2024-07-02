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
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app, locale_selector="en")


class Config():
    """
    used to set Babel’s default locale ("en") and timezone ("UTC").
    used as config for your Flask app.
    """
    LANGUAGES = ["en", "fr"]
