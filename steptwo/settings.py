import sys
import os
from django.conf import settings

DEBUG = os.environ.get('DEBUG', 'on') == 'on'
SECRET_KEY = os.environ.get('SECRET_KEY')
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '192.168.33.11').split(',')
DEBUG=DEBUG
ROOT_URLCONF='app'
SECRET_KEY=SECRET_KEY
ALLOWED_HOSTS=ALLOWED_HOSTS
MIDDLEWARE_CLASSES=(
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware'
)