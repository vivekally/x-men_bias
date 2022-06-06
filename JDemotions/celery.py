from __future__ import absolute_import, unicode_literals

import os

import configurations
from celery import Celery
from celery.signals import before_task_publish, task_postrun, task_prerun

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'JDemotions.settings')
os.environ.setdefault('DJANGO_CONFIGURATION', 'Development')

configurations.setup()

# register django-origin-trail signals

# celery apps
app = Celery('JDemotions')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('JDemotions.settings.celery_settings:CELERY_SETTINGS')

# Load task modules from all registered Django apps configs.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
