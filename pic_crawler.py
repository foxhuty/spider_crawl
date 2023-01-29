# -*- codeing = utf-8 -*-
# @Time: 2022/3/12 21:44
# @Author: Foxhuty
# @File: pic_crawler.py
# @Software: PyCharm
# @Based on python 3.10
import threading

import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
import os

dirName = r'D:/爬虫数据/umeipic/'
if not os.path.exists(dirName):
    os.mkdir(dirName)


# url = "https://www.umeitu.com/meinvtupian/xingganmeinv/246429.htm"


def download_pic(url):
    response = requests.get(url)
    response.encoding = 'utf-8'
    # print(response.text)
    # 把源码交给bs4处理
    main_page = BeautifulSoup(response.text, 'html.parser')
    a_list = main_page.find('div', class_='TypeList').find_all('a')
    for a in tqdm(a_list):
        href = a.get('href')
        # print(href)
        child_page_resp = requests.get('https://www.umeitu.com/' + href)
        child_page_resp.encoding = 'utf-8'  # 处理乱码
        child_page_text = child_page_resp.text
        # 从子页面中拿到图片下载路径
        child_page = BeautifulSoup(child_page_text, 'html.parser')
        p = child_page.find('p', align='center')
        img = p.find('img')
        src = img.get('src')  # 直接通过get就可以得到属性值
        # 下载图片
        img_resp = requests.get(src)
        # img_resp.content
        img_name = src.split('/')[-1]
        with open(dirName + img_name, mode='wb') as f:
            f.write(img_resp.content)


def main():
    for i in range(1, 10):
        if i == 1:
            url = "https://www.umeitu.com/bizhitupian/weimeibizhi/"
            download_pic(url)
        else:
            url = "https://www.umeitu.com/bizhitupian/weimeibizhi/index_" + str(i) + ".html"
            download_pic(url)


if __name__ == '__main__':
    t = threading.Thread(target=main)
    t.start()
    # main()
