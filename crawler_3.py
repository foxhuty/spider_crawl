# -*- codeing = utf-8 -*-
# @Time: 2022/2/15 15:29
# @Author: Foxhuty
# @File: crawler_3.py
# @Software: PyCharm
# @Based on python 3.10

import requests


"""
用post方法获取网页内容
"""

url = 'https://fanyi.baidu.com/sug'
word = input('enter your word:')
data = {'kw': word}
# 发送post请求,发送的数据必须在字典中，通过data参数进行传递
respond = requests.post(url, data=data)
# page_text=respond.content.decode(encoding='utf-8')
page_text = respond.json()  # 将服务器返回的内容直接处理成json()==>dict
print(page_text['data'])
for item in page_text['data']:
    print(f"{item['k']}: {item['v']}")
