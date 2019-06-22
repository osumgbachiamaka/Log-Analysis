#!/usr/bin/env Python 2.7.16rc1
from flask import Flask, render_template
from database import get_views, get_authors, error_percentage

app = Flask(__name__)


@app.route('/')
def index():
    most_viewers = get_views()
    authors = get_authors()
    percentage = error_percentage()
    return render_template('index.html', results=most_viewers,
                           authors=authors, percentage=percentage)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
