from os import getenv

import dotenv

from src.api.settings import DEBUG

dotenv.load_dotenv()

DATABASES = {
    'default': {
        'ENGINE': getenv('PG_ENGINE'),
        'NAME': getenv('PG_DATABASE'),
        'USER': getenv('PG_USER') if DEBUG else getenv('PG_USER_PROD'),
        'PASSWORD': getenv('PG_PASSWORD')
        if DEBUG
        else getenv('PG_PASSWORD_PROD'),
        'HOST': getenv('PG_HOST') if DEBUG else getenv('PG_HOST_PROD'),
        'PORT': getenv('PG_PORT'),
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/0',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
            'PASSWORD': getenv('REDIS_PASS'),
            'COMPRESSOR': 'django_redis.compressors.zlib.ZlibCompressor',
        },
    }
}

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            'hosts': [('localhost', '6379')],
        },
    },
}

SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
SESSION_CACHE_ALIAS = 'default'
CACHE_TTL = 60 * 1

REDIS_HOST = 'localhost'
REDIS_PORT = 6379
