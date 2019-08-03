# 练习：Kenneth 今天 Star 了哪些库: 试着用所学知识去发现 Kenneth 今天 Starred 了哪些库，并且自动在浏览器中打开这些库的地址。

import requests
import webbrowser
import time


api = 'https://api.github.com/users/kennethreitz/starred'

info = requests.get(api).json()
starred = []
for i in info:
    starred.append(i['id'])
# 测试
print(starred)
print(len(starred))
print(type(info))

while True:

    info = requests.get(api).json()
    if i in info:
        if not i['id'] in info:
            starred.append(i['id'])
            repo_name = i['name']
            owner = i['owner']['login']
            webpage = "https://github.com/" + owner + "/" + repo_name
            webbrowser.open(webpage)
    time.sleep(600)