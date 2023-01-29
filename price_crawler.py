# -*- codeing = utf-8 -*-
# @Time: 2022/3/12 16:22
# @Author: Foxhuty
# @File: price_crawler.py
# @Software: PyCharm
# @Based on python 3.10
import re
import requests
from bs4 import BeautifulSoup

url = "http://www.vegnet.com.cn/Price/List?marketID=3&year=2021&month=12&day=28"
respond = requests.get(url)

page = BeautifulSoup(respond.text, 'html.parser')
page_price = page.find('div', attrs={"class": "jxs_list price_l"})
# print(page_price)
page_ps = page_price.find_all('p')[1:]

for p in page_ps:
    line=p.text.split(' ')
    vegetables=line[0:1][0].strip('\n')
    print(vegetables)
    obj=re.compile(r"\d+[-]\d+[-]\d+",re.S)

    date=obj.findall(vegetables)
    name=re.findall(r".*?](?P<v_name>.*?)",vegetables)
    print(date)

    # date = p.find('span', class_='k_1').text
    # name = p.find('span', class_='k_2').text
    # market = p.find('span', class_='k_3').text
    # # min = p.find('span', class_='k_4').text
    # print(date,name,market)

