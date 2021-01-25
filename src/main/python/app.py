import logging
import os
from pathlib import Path

from flask import Flask, render_template

from logging_conf import setup
from news.news_site.api.news_api import make_simple_news_html

app = Flask(__name__)

setup(json_enabled=True)

app_logger = logging.getLogger("ravnml")


@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")


@app.route('/hello-world', methods=['GET', 'POST'])
def hello_world():
    greeting_target = os.environ.get('GREETING_TARGET', 'World')
    return 'Hello {}!\n'.format(greeting_target)


@app.route('/headlines', methods=['GET'])
def headlines():
    make_simple_news_html(Path('templates/headlines.html'))
    return render_template("headlines.html")


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
