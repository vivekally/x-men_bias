_log_format = (
    '%(asctime)apps %(levelname)apps '
    '[pid: %(process)apps] [%(name)apps: %(lineno)apps] '
    '%(message)apps'
)


class LoggerSettingsMixin(object):
    LOGGING = {
        'version': 1,
        'formatters': {
            'verbose': {
                'format': _log_format,
            },
        },

        'handlers': {
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'verbose',
            },
        },
        'loggers': {
            'django': {
                'handlers': ['console'],
                'level': 'DEBUG'
            },
            'django.template': {
                'handlers': ['console'],
                'level': 'INFO',
                'propagate': False,
            },
            'statsd': {
                'handlers': ['console'],
                'level': 'DEBUG',
                'propagate': True,
            },
            'django.db.backends': {'level': 'INFO'},
            'django.utils.autoreload': {'level': 'INFO'},
        }
    }
