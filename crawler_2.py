# -*- codeing = utf-8 -*-
# @Time: 2022/2/15 15:14
# @Author: Foxhuty
# @File: crawler_2.py
# @Software: PyCharm
# @Based on python 3.10

import requests

"""
用get方法获取网页内容
"""
query = input('please enter an item for crawling:')
url = f'https://www.sogou.com/web?query={query}'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'}
respond=requests.get(url,headers=headers)
# page_script=respond.text
page_script=respond.content.decode()
print(page_script)

# name = ''.join(['成华区', '青羊区'])
# lst='成华'.split('，')
# print(lst)
#
# print(name)
# if '成华' or '锦江' in name:
#     print('yes')
