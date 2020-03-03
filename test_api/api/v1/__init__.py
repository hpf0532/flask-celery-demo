from flask import Blueprint
from flask_cors import CORS
#from test_api.tasks import apptask

api_v1 = Blueprint('api_v1', __name__)

CORS(api_v1)

from test_api.api.v1 import views
