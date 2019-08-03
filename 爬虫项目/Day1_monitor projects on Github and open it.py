#  api: https://api.github.com/repos/huge-success/sanic
#  web_page: https://github.com/huge-success/sanic

import requests
import webbrowser
import time
import json

api = 'https://api.github.com/repos/huge-success/sanic'
webpage = 'https://github.com/huge-success/sanic'
last_update = '2018-07-31T18:44:52Z'
all_info = requests.get(api).json()
"""
all_info = requests.get()  # 得到接口所有信息
dict_info = all_info.json()  # 把json数据转化成python数据存储在字典
"""
cur_update = all_info['updated_at']

while True:

    if last_update is None:
        last_update = cur_update

    if last_update < cur_update:
        webbrowser.open(webpage)
    time.sleep(600)