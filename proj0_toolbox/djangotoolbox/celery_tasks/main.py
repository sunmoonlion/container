from celery import Celery
import os

# 读取django项目的配置
os.environ["DJANGO_SETTINGS_MODULE"] = "djangotoolbox.settings.dev"

# 创建Celery实例
celery_app = Celery('djangotoolbox')

# 加载配置
celery_app.config_from_object('celery_tasks.config')

# 加载可用的任务
celery_app.autodiscover_tasks([
    'celery_tasks.sms',
    'celery_tasks.email_active',
])
