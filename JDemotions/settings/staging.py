from JDemotions.settings.base import Base

import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration
from sentry_sdk.integrations.celery import CeleryIntegration


class Staging(Base):
    SECRET_KEY = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
    DEBUG = False
    ALLOWED_HOSTS = [
        'JDemotions.stg.blng.io',
    ]

    @classmethod
    def pre_setup(cls):
        super(Staging, cls).pre_setup()
        cls.MIDDLEWARE += [
            # datadog middleware
            'django_dogstatsd.middleware.RequestStatusMiddleware',
            'django_dogstatsd.middleware.RequestTimingMiddleware',
            'django_dogstatsd.middleware.RequestErrorLogMiddleware',
        ]

        sentry_sdk.init(
            dsn="https://XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX@sentry.io/XXXXXXX",
            max_breadcrumbs=50,
            attach_stacktrace=True,
            environment="staging",
            integrations=[DjangoIntegration(), CeleryIntegration()]
        )
