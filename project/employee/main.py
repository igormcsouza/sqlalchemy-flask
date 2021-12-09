from flask import Blueprint
from flask.app import Flask

from project.employee import view


bp = Blueprint("employee", __name__, url_prefix="/employee")
bp.add_url_rule("/", view_func=view.index, methods=["GET"])


def init_app(app: Flask):
    app.register_blueprint(bp)