#!/usr/bin/env python
# ------------------------------------------------------------------------------
#  Copyright (c) 2019. Anas Abu Farraj
# ------------------------------------------------------------------------------
"""Learning REST API with Flask and Python."""

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello, Index!</h1>'


if __name__ == '__main__':
    app.run()
