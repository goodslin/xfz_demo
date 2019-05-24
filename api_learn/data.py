from django import setup
import os

# 在环境变量中设置配置文件
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api_learn.settings')
# 加载配置文件
setup()

from rest_learn.models import TestModel

data_set = {
    'ls': """import os\r\nprint(os.listdir())""",
    'pwd': """import os\r\nprint(os.getcwd())""",
    'hello world': """print('Hello world')"""
}
for name, code in data_set.items():
    TestModel.objects.create(name=name, code=code)

print('Done')
