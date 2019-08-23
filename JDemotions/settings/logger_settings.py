_log_format = (
    '%(asctime)apps %(levelname)apps '
    '[pid: %(process)apps] [%(name)apps: %(lineno)apps] '
    '[oid: %(origin_id)apps] '
    '[strail: %(service_trail)apps] '
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
        'filters': {
            'origin_id': {
                '()': 'django_origin_trail.logging_filters.OriginIdFilter'
            },
            'service_trail': {
                '()': 'django_origin_trail.logging_filters.ServiceTrailFilter'
            }
        },

        'handlers': {
            'console': {
                'level': 'DEBUG',
                'filters': ['origin_id', 'service_trail'],
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
