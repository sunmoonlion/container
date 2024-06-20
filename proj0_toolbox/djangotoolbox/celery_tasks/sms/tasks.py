# 定义任务
from .ccp_sms import CCP
from . import constants
from celery_tasks.main import celery_app


# 使用装饰器装饰异步任务，保证celery识别任务
@celery_app.task(name='send_sms_code')
def send_sms_code(mobile, sms_code):
    """
    发送短信验证码的异步任务
    :param mobile: 手机号
    :param sms_code: 短信验证码
    :return: 成功：0 、 失败：-1
    """
    send_ret = CCP().send_template_sms(constants.SEND_SMS_TEMPLATE_ID, mobile, (sms_code, constants.SMS_CODE_EXPIRES))
    return send_ret