# -*- codeing = utf-8 -*-
# @Time: 2022/2/15 16:02
# @Author: Foxhuty
# @File: crawler_4.py
# @Software: PyCharm
# @Based on python 3.10
import requests
import json
from xml import etree

url = "https://movie.douban.com/j/chart/top_list"

# 重新封装参数
params = {
    "type": "24",
    "interval_id": "100:90",
    "action": "",
    "start": 1,
    "limit": 20,
}
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
}
restpond = requests.get(url=url, params=params, headers=headers)
# print(restpond.url) #得到与url后带的参数一样
# print(restpond.request.headers)
page_html = restpond.json()
print(page_html)
# page_list=json.dumps(page_html)
# print(page_list)
restpond.close()
