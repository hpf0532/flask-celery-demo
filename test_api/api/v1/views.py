from flask import jsonify
from celery_task.tasks import apptask
from test_api.api.v1 import api_v1
from test_api.extensions import db
from flask import current_app

@api_v1.route("/", methods=["GET"])
def index():
    r = apptask.apply_async()
    return jsonify({"status": "success"})
