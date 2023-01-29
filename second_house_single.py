# -*- codeing = utf-8 -*-
# @Time: 2022/3/21 1:03
# @Author: Foxhuty
# @File: second_house_single.py
# @Software: PyCharm
# @Based on python 3.10
import time
import requests
from lxml import etree
from threading import Thread

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36"
}


def down_load(url):
    page_text = requests.get(url=url, headers=headers).text
    print(page_text)
    tree = etree.HTML(page_text)
    # print(tree)
    divs = tree.xpath('//*[@id="__layout"]/div/section/section[3]/section[1]/section[2]/div')

    file = open(r"D:\爬虫数据\成都二手房价3333.txt", mode='a', encoding='utf-8')
    for div in divs:
        house = div.xpath('./a/div[2]//h3/text()')[0]
        price = div.xpath('./a/div[2]/div[2]/p[1]/span/text()')
        price = price[0] + "万元" if len(price) > 0 else ""
        print(house, price)
        file.write(f'{house},\t{price}\n')
        # print(f'{house},\t{price}\n')
    file.close()


def main():
    for page in range(1, 3):
        url = f"https://cd.58.com/ershoufang/p+{str(page)}/"
        down_load(url)
        print(f'第{page}完成')
        time.sleep(2)


if __name__ == '__main__':
    t=Thread(main())
    t.start()

    # main()
