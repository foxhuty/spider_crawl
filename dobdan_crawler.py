# -*- codeing = utf-8 -*-
# @Time: 2022/3/12 12:56
# @Author: Foxhuty
# @File: dobdan_crawler.py
# @Software: PyCharm
# @Based on python 3.10
import requests
import re
import csv

# 页面源代码
url = "https://movie.douban.com/top250?start=0"
obj_pattern = re.compile(r'<li>.*?<div class="pic">.*?<span class="title">(?P<name>.*?)</span>'
                         # r'.*?</span>.*?</span>.*?<p class>"(?P<director>.*?)&nbsp;&nbsp'
                         r'.*?<br>(?P<year>.*?)&nbsp'
                         r'.*?<span class="rating_num" property="v:average">(?P<rating>.*?)</span>'
                         r'.*?<span>(?P<persons>.*?人评价)</span>', re.S)


def get_html(url):
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"
    }
    respond = requests.get(url, headers=headers)
    page_content = respond.text
    return page_content


def get_content_by_re(obj):
    page_content = get_html(url)
    result = obj.finditer(page_content)
    file = open(r"D:\成绩统计结果\电影评价.csv", mode='w')
    csv_writer = csv.writer(file)
    for it in result:
        print(it.group('name'))
        # print(it.group('director'))
        print(it.group('rating'))
        print(it.group('persons'))
        print(it.group('year').strip())
        dic = it.groupdict()
        dic['year'] = dic['year'].strip()
        csv_writer.writerow((dic.values()))
    file.close()
    print('successfully done')



file = open(r"D:\成绩统计结果\电影评价.csv", mode='w')
csv_writer = csv.writer(file)
for i in range(0, 250, 25):
    url = "https://movie.douban.com/top250?start=" + str(i)
    page = get_html(url)
    result = obj_pattern.finditer(page)
    for it in result:
        dic = it.groupdict()
        dic['year'] = dic['year'].strip()
        csv_writer.writerow(dic.values())

file.close()
