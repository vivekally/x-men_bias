from __future__ import absolute_import, unicode_literals

import os

import configurations
from celery import Celery
from celery.signals import before_task_publish, task_postrun, task_prerun
from django_origin_trail.celery_signals import set_logger_params, set_task_local_context, delete_task_local_context

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'JDemotions.settings')
os.environ.setdefault('DJANGO_CONFIGURATION', 'Development')

configurations.setup()

# register django-origin-trail signals
before_task_publish.connect(set_logger_params)
task_prerun.connect(set_task_local_context)
task_postrun.connect(delete_task_local_context)

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
