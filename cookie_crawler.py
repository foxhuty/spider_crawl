# -*- codeing = utf-8 -*-
# @Time: 2022/3/15 22:20
# @Author: Foxhuty
# @File: cookie_crawler.py
# @Software: PyCharm
# @Based on python 3.10

import requests

# 会话
session = requests.session()
data = {
    "loginName": "18982186799",
    "password": "fox081126fox"
}

# 1.登录
url = "https://passport.17k.com/login"

session.post(url, data=data)
# 2.获取书架上的书
resp = session.get('https://user.17k.com/www/bookshelf/')
resp.encoding='utf-8'
print(resp.text)
