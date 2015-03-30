# coding: utf-8
import os
from config_parser.parser import ConfigParser

__author__ = 'damirazo <me@damirazo.ru>'


# Путь до текущего приложение
APP_ROOT = os.path.abspath(os.path.dirname(__file__))
# Глобальный путь до проекта
PROJECT_ROOT = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..')
# Путь до директории с шаблонами
TEMPLATES_ROOT = os.path.join(PROJECT_ROOT, 'templates')
# Путь до директории с данными
DATA_ROOT = os.path.join(PROJECT_ROOT, 'data')
# Путь до директории со статичными файлами
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')


# Объект парсера конфигурационного файла
parser = ConfigParser(file_path=os.path.join(DATA_ROOT, 'config.json'))


# Настройки разработки
DEBUG = TEMPLATE_DEBUG = parser.get_bool('system.development.debug')
ALLOWED_HOSTS = parser.get('system.development.allowed_hosts', ())
SECRET_KEY = parser.get('system.secret_key')


# Список доступных модулей
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)
INSTALLED_APPS += parser.get('system.apps', ())


# Список классов-посредников
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)
MIDDLEWARE_CLASSES += parser.get('system.middlewares', ())


# Настройки для запуска
ROOT_URLCONF = 'blank.urls'
WSGI_APPLICATION = 'application.wsgi.application'


# Список настроек БД
DATABASES = {}
for name, params in parser.get('system.databases', {}).items():
    DATABASES[name] = {
        'ENGINE': params['engine'],
        'NAME': params['name'],
        'HOST': params['host'],
        'PORT': params['port'],
        'USER': params['user'],
        'PASSWORD': params['password'],
    }


# Используемый по умолчанию язык
LANGUAGE_CODE = 'ru-RU'


# Настройки интернационализации и временных зон
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# URL для статики
STATIC_URL = '/static/'


# Перечисление путей до шаблонов
TEMPLATE_DIRS = (
    TEMPLATES_ROOT,
)