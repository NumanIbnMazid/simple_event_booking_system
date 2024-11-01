# project/celery.py
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings
from config import config

if config.MODE == "PRODUCTION":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings.production")
else:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings.development")
    
app = Celery("Event Booking System")

app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f"Request: {self.request!r}")
