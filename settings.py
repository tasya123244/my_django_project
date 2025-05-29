import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'ваш-секретный-ключ'  # Можно сгенерировать новый

DEBUG = True

ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    'BodrovaApp',
    'hse_education',
]

MIDDLEWARE = [

]

ROOT_URLCONF = 'urls'  # Измените если используете другую структуру

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'memory',
    }
}

STATIC_URL = '/static/'

# settings.py
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
