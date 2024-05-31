from flask import Flask
import os
import json


# 配置对象方式加载配置信息
class DefaultConfig(object):
    """
    默认配置
    """
    SECRET_KEY = 'hohph'

#
# class DevelopmentConfig(DefaultConfig):
#     DEBUG = True


class ProductionConfig(DefaultConfig):
    DEBUG = True
    
def create_flask_app(config):
    """构建flask对象的工厂函数"""
    app = Flask(__name__, static_url_path='/static', static_folder='static_files')

    # 设置应用的配置。该配置会被下面的从文件或环境变量加载的配置覆盖！
    app.config.from_object(config)

    # 检查环境变量 'PROJECT_SETTING' 是否已设置
    setting_env_var = os.getenv('PROJECT_SETTING')
    if setting_env_var:
        app.config.from_envvar('PROJECT_SETTING')
    else:
        # 下面的setting.py文件是一个配置文件，它的路径可能不同于上面的环境变量指定的配置文件路径，这是两个概念，应用的方法也不同：前者是app.from_envvar,后者是app.from_pyfile(setting.py一定是PY文件)
        # default_config_path = '/path/to/your/default/config/setting.py' #绝对路径
        default_config_path = 'setting.py' #相对路径
        if os.path.exists(default_config_path):
            app.config.from_pyfile(default_config_path)
            print(f"Loaded default configuration from {default_config_path}")
        else:
            print(f"Warning: The environment variable 'setting' is not set and the default configuration file '{default_config_path}' does not exist.")

    return app


app = create_flask_app(ProductionConfig)

# app = create_flask_app(DevelopmentConfig)


# 定义视图
@app.route('/')
def index():
    # 读取配置信息
    print(app.config['SECRET_KEY'])
    return 'hello world'

print(app.url_map)  # -> Map对象
# 需求需要遍历url_map  取出特定信息 在一个特定的接口返回
# for rule in app.url_map.iter_rules():
#     print('name={} path={}'.format(rule.endpoint, rule.rule))
# endpoint -> 视图函数名
# rule -> 路径

# @app.route('/')
# def route_map():
#     """
#     主视图，返回所有视图网址
#     """
#     rules_iterator = app.url_map.iter_rules()
#     # {'index': '/', 'static': '/s/xxx}
#     return json.dumps({rule.endpoint: rule.rule for rule in rules_iterator})





# if __name__ == '__main__':
#     # 运行flask提供的调试服务器
#     app.run(host="0.0.0.0", port=8000)
# 现在一般在命令行以如下方式启动项目：
# flask run  <===>  python -m flask run