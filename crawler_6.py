# -*- coding: utf-8 -*-
# @Time: 2022/9/12 3:51
# @Author: foxhuty
# @File: crawler_6.py
# @Software: PyCharm
# @Based on: python 3.10.6

import requests
from lxml import etree


def get_url(url):
    domain = "https://desk.zol.com.cn"
    response = requests.get(url)
    response.encoding = 'gbk'
    # print(response.text)
    tree = etree.HTML(response.text)
    href_list = tree.xpath("//ul[@class='pic-list2  clearfix']//a/@href")
    for href in href_list:
        if str(href).endswith('html'):
            new_href = domain + href
            print(new_href)


if __name__ == '__main__':
    for page in range(1, 21):
        page_url = f"https://desk.zol.com.cn/pc/{page}.html"
        print(f'第{page}页url')
        get_url(page_url)
