import logging
import os
from pathlib import Path

from flask import Flask, render_template

from underload.logger.logging_conf import setup
from underload.news.news_site.api.news_api.key import get_key
from underload.news.news_site.api.news_api.main import Client

setup(json_enabled=False)
app_logger = logging.getLogger("underload")

client = Client(get_key())

flask_lib_path = Path('underload/templates/')
docker_lib_path = Path('/usr/local/lib/python3.6/site-packages/underload/')


def create_app(test_config=None, instance_path=None):
    # app = Flask(__name__, template_folder=TEMPLATE_FOLDER, static_url_path=STATIC_FOLDER)
    app = Flask(__name__)

    @app.route('/', methods=['GET'])
    def index():
        return render_template("index.html")

    @app.route('/headlines', methods=['GET'])
    def headlines():
        client.get_news().to_html_to_file(docker_lib_path.joinpath('templates/headlines.html'))
        return render_template("headlines.html")

    @app.route('/tailor', methods=['GET'])
    def tailor():
        client.tailored_news().to_html_to_file(docker_lib_path.joinpath('templates/tailor.html'))
        return render_template("tailor.html")

    # USED FOR TESTING
    @app.route('/test', methods=['GET'])
    def test():
        client.testing().to_html_to_file(docker_lib_path.joinpath('templates/test.html'))
        return render_template("test.html")

    return app
