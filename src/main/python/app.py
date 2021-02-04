import logging
import os
from pathlib import Path

from flask import Flask, render_template

from logging_conf import setup
from helpers import interests
from news.news_site.api.news_api.key import get_key
from news.news_site.api.news_api.main import Client

TEMPLATE_FOLDER = os.getenv('TEMPLATE_FOLDER', '../docker/templates')
# TEMPLATE_FOLDER = os.getenv('TEMPLATE_FOLDER', 'templates')
STATIC_FOLDER = os.getenv('STATIC_FOLDER', '/static')

app = Flask(__name__, template_folder=TEMPLATE_FOLDER, static_url_path=STATIC_FOLDER)

setup(json_enabled=True)

app_logger = logging.getLogger("ravnml")

app_logger.info(f'Template folder is set to [{TEMPLATE_FOLDER}]')
app_logger.info(f'Current dir [{os.getcwd()}]')

client = Client(get_key())


@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")


@app.route('/hello-world', methods=['GET', 'POST'])
def hello_world():
    greeting_target = os.environ.get('GREETING_TARGET', 'World')
    return 'Hello {}!\n'.format(greeting_target)


@app.route('/headlines', methods=['GET'])
def headlines():
    client.get_news().to_html_to_file(Path(f'{TEMPLATE_FOLDER}/headlines.html'))
    return render_template("headlines.html")


@app.route('/tailor', methods=['GET'])
def tailor():
    client.tailored_news().to_html_to_file(Path(f'{TEMPLATE_FOLDER}/tailor.html'))
    return render_template("tailor.html")


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
