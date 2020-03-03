import datetime
import time
import os
import random
from flask import current_app
from test_api.models import User
from test_api.extensions import db

from celery_task import celery, MyTask


@celery.task(bind=True, base=MyTask)
def apptask(self):
    print(current_app.config)
    print("==============%s " % current_app.config["SQLALCHEMY_DATABASE_URI"])
    print("++++++++++++++%s " % os.getenv("DATABASE_URL"))
    time.sleep(5)
    user = User(username="user%s" % random.randint(1,100))
    db.session.add(user)
    db.session.commit()
    return 'success'
