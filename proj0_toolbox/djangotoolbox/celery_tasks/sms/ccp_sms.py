import json
from ronglian_sms_sdk import SmsSDK

accId = '8aaf0708732220a60174480516e87d2a'
accToken = '7654f9830ae04d9682dccae0ac5db8fa'
#使用测试app,如果生产环境则要替换
appId = '8aaf0708732220a60174480517aa7d30'


class CCP(object):
    """发送短信验证码的单例类"""

    def __new__(cls, *args, **kwargs):
        """
        定义单例的初始化方法
        :return: 单例
        """
        # 判断单例是否存在：_instance属性中存储的就是单例
        if not hasattr(cls, '_instance'):
            # 如果单例不存在，初始化单例
            cls._instance = super(CCP, cls).__new__(cls, *args, **kwargs)

            # 初始化SmsSDK
            cls._instance.sdk = SmsSDK(accId, accToken, appId)

        # 返回单例
        return cls._instance

    def send_template_sms(self, tid,mobile,datas):
        """
        发送短信验证码单例方法
        :param tid: 模板ID
        :param mobile: 手机号
        :param datas: 内容数据
        :return: 成功：0 失败：-1
        """        
        result = self.sdk.sendMessage(tid, mobile, datas)
        #result是字符串，转为字典
        result_dict = json.loads(result)
        if result_dict.get('statusCode') == '000000':
            return 0
        else:
            return -1





if __name__ == '__main__':
    # 注意： 测试的短信模板编号为1
    tid = '1'
    mobile = '13701819268'
    #测试变量为1-4的数字
    datas = ('1234',4)
    # 单例类发送短信验证码
    CCP().send_template_sms(tid, mobile, datas)
