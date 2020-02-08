import traceback

from flask import Flask, request

import config
from common.log import Logger
from common.response import Response
from view.summary import summary_bp
from view.sync_api import sync_bp

app = Flask(__name__)
app.config.from_object(config)
log = Logger(__name__)

app.register_blueprint(sync_bp, url_prefix='/sync')
app.register_blueprint(summary_bp, url_prefix='/summary')


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.before_request
def before_request():
    log.info(request)


@app.after_request
def after_request(response):
    if response.json:
        log.info(response)
    return response


@app.teardown_request
def teardown_request(error):
    if error is not None:
        log.error(error)


@app.errorhandler(Exception)
def error_handler(exception: Exception):
    if exception:
        log.error(traceback.format_exc())
        return Response.failed(msg=f'{exception}')


if __name__ == '__main__':
    app.run()
