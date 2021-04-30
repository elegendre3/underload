import logging
import os
from pathlib import Path

from flask import Flask, render_template

from underload.logger.logging_conf import setup
from underload.news.news_site.api.news_api.key import get_key
from underload.news.news_site.api.news_api.main import Client

setup(json_enabled=False)
app_logger = logging.getLogger("underload")

# TEMPLATE_FOLDER = os.getenv('TEMPLATE_FOLDER', '../docker/templates')
# STATIC_FOLDER = os.getenv('STATIC_FOLDER', '/static')
#
# app = Flask(__name__, template_folder=TEMPLATE_FOLDER, static_url_path=STATIC_FOLDER)

# app_logger.info(f'Template folder is set to [{TEMPLATE_FOLDER}]')
# app_logger.info(f'Current dir [{os.getcwd()}]')

client = Client(get_key())


def create_app(test_config=None, instance_path=None):
    app = Flask(__name__)

    @app.route('/', methods=['GET'])
    def index():
        return render_template("index.html")

    @app.route('/headlines', methods=['GET'])
    def headlines():
        client.get_news().to_html_to_file(Path(f'{TEMPLATE_FOLDER}/headlines.html'))
        return render_template("headlines.html")

    @app.route('/tailor', methods=['GET'])
    def tailor():
        client.tailored_news().to_html_to_file(Path(f'{TEMPLATE_FOLDER}/tailor.html'))
        return render_template("tailor.html")

    # USED FOR TESTING
    @app.route('/test', methods=['GET'])
    def test():
        client.testing().to_html_to_file(Path(f'{TEMPLATE_FOLDER}/test.html'))
        return render_template("test.html")

    return app
