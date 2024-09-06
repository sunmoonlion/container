"""
Django settings for djangotoolbox project.

Generated by 'django-admin startproject' using Django 5.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""
from datetime import timedelta
import os,sys
from pathlib import Path


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# 追加导包路径指向apps包
# sys.path.insert(0, '/home/zym/Documents/projects/meiduo_project/meiduo_mall/meiduo_mall/apps')
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-%)@6^n*#so%w!(fye%(%nmh*4u^(#c9l65o-8hzj1dj$$$8@i1'
# 示例：定义一个 salt，确保是 bytes 类型
EMAIL_TOKEN_SALT = b'your_salt_value_here'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'users',
    'contents',
    'verifications',
    'areas',
    'django_filters',
    'toolbox_admin',
    'corsheaders',  # 跨域模块
    'rest_framework',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'djangotoolbox.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.jinja2.Jinja2',
        'DIRS': [BASE_DIR/'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'environment': 'utils.jinja2_env.jinja2_environment',
        },
    },
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
    }
]

WSGI_APPLICATION = 'djangotoolbox.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {#写（主机）
        'ENGINE': 'django.db.backends.mysql',  # 数据库引擎
        'HOST': '47.103.135.26',  # 数据库主机
        'PORT': 3300,  # 数据库端口
        'USER': 'myrt',  # 数据库用户名
        'PASSWORD': '123456',  # 数据库用户密码
        'NAME': 'mydb'  # 数据库名字
    },
    'slave': {#读（从机）
        'ENGINE': 'django.db.backends.mysql',  # 数据库引擎
        'HOST': '47.100.19.119',  # 数据库主机
        'PORT': 4300,  # 数据库端口
        'USER': 'myrt',  # 数据库用户名
        'PASSWORD': '123456',  # 数据库用户密码
        'NAME': 'mydb' # 数据库名字
    }
}

CACHES = {
    "default": {  # 默认
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://47.103.135.26:6370/0",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },
    "session": {  # session
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://47.103.135.26:6370/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },
    "verify_code": {  # 验证码
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://47.103.135.26:6370/2",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },
}

SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "session"


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# 配置工程日志
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,  # 是否禁用已经存在的日志器
    'formatters': {  # 日志信息显示的格式
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(lineno)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(module)s %(lineno)d %(message)s'
        },
    },
    'filters': {  # 对日志进行过滤
        'require_debug_true': {  # django在debug模式下才输出日志
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {  # 日志处理方法
        'console': {  # 向终端中输出日志
            'level': 'INFO',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'file': {  # 向文件中输出日志
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': BASE_DIR / 'logs/mydb.log',  # 日志文件的位置
            'maxBytes': 300 * 1024 * 1024,
            'backupCount': 10,
            'formatter': 'verbose'
        },
    },
    'loggers': {  # 日志器
        'django': {  # 定义了一个名为django的日志器
            'handlers': ['console', 'file'],  # 可以同时向终端与文件中输出日志
            'propagate': True,  # 是否继续传递日志信息
            'level': 'INFO',  # 日志器接收的最低日志级别
        },
    }
}


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

# 配置开发时静态文件加载路径
STATICFILES_DIRS = [BASE_DIR, 'static']

# 设置STATIC ROOT 和 STATIC URL（注意，收集时的目录和开发时的存储目录（也是加载目录）是不同的，这点不同于媒体文件）
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = "/static/"

# 设置MEDIA ROOT 和 MEDIA URL(请注意：这里meidia_root指定的目录是收集时的目录，因为它就是开发阶段的媒体默认存储目录，所以，收集时没有变化)
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = "/media/"
# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# 指定自定义的用户模型类：值的语法 ==> '子应用.用户模型类'
AUTH_USER_MODEL = 'users.User'

# 指定自定义用户认证后端
# AUTHENTICATION_BACKENDS = ['users.utils.UsernameMobileBackend']
AUTHENTICATION_BACKENDS = ['users.utils.DjangotoolboxModelBackend']

# 判断用户是否登录后，指定未登录用户重定向的地址
LOGIN_URL = '/login/'

# 邮件参数
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'  # 导入邮件模块
EMAIL_HOST = 'smtp.qq.com'  # 发邮件主机
EMAIL_PORT = 587  # 发邮件端口
EMAIL_HOST_USER = '1668372030@qq.com'  # 授权的邮箱
EMAIL_HOST_PASSWORD = 'nwhigfhhunqbbafg'  # 邮箱授权时获得的密码，非注册登录密码
EMAIL_FROM = 'djangotoolbox<1668372030@qq.com>'  # 发件人抬头
# # 邮件参数
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'  # 导入邮件模块
# EMAIL_HOST = 'smtp.163.com'  # 发邮件主机
# EMAIL_PORT = 25  # 发邮件端口
# EMAIL_HOST_USER = '13701819268@163.com'  # 授权的邮箱
# EMAIL_HOST_PASSWORD = 'YNWKCEMEYLJDRVSF'  # 邮箱授权时获得的密码，非注册登录密码
# EMAIL_FROM = 'djangotoolbox<13701819268@163.com>'  # 发件人抬头

# 邮箱验证链接
EMAIL_VERIFY_URL = 'http://47.100.19.119:8000/emails/verification/'

# 指定自定义的Django文件存储类
DEFAULT_FILE_STORAGE = 'utils.fastdfs.fdfs_storage.FastDFSStorage'
FDFS_CLIENT_CONF = os.path.join(BASE_DIR, 'utils/fastdfs/client.conf')
# FastDFS相关参数
FDFS_BASE_URL = 'http://47.103.135.26:8080/'

# 配置本地存储
LOCAL_STORAGE = 'utils.local_storage.LocalStorage'

# # CORS
# CORS_ORIGIN_WHITELIST = (
#     '127.0.0.1:8080',
#     'localhost:8080',
# )
CORS_ORIGIN_ALLOW_ALL = True
#
CORS_ALLOW_CREDENTIALS = True  # 允许携带cookie

CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
]

REST_FRAMEWORK = {

    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend'
    ],


    'DEFAULT_AUTHENTICATION_CLASSES': (
        #'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',

        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,
    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,
    'AUTH_HEADER_TYPES': ('Bearer',),
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',
    'JTI_CLAIM': 'jti',
}

