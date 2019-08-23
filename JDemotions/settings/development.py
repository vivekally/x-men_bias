from JDemotions.settings.base import Base


class Development(Base):
    SECRET_KEY = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
    ALLOWED_HOSTS = [
        '127.0.0.1',
        'JDemotions.dev.blng',
    ]
