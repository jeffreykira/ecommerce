import logging
from ecommerce import util
from flask import Flask, Blueprint, request, g

log = logging.getLogger(__name__)
flask_app = Flask(__name__)


@util.log_scope(log)
def init(config_obj):
    flask_app.config.from_object(config_obj)

    blueprint = Blueprint('api', __name__, url_prefix='/api/v1')
