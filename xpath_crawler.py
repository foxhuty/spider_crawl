# -*- codeing = utf-8 -*-
# @Time: 2022/3/12 23:02
# @Author: Foxhuty
# @File: xpath_crawler.py
# @Software: PyCharm
# @Based on python 3.10
import requests
from lxml import etree
from tqdm import tqdm


def get_html(url):
    response = requests.get(url)
    response.encoding = 'utf-8'
    main_page = response.text
    print(main_page)
    return main_page


def crawling_data(main_page):
    html = etree.HTML(main_page)
    divs = html.xpath(r'/html/body/div[6]/div/div/div[2]/div[5]/div[1]/div')
    file = open(r"D:\成绩统计结果\程序服务信息.txt", mode='w',encoding='utf-8')
    for div in divs:
        price = div.xpath("./div/div/a[2]/div[2]/div[1]/span[1]/text()")[0].strip('¥')
        title = "SAAS".join(div.xpath("./div/div/a[2]/div[2]/div[2]/p/text()"))
        company = div.xpath("./div/div/a[1]/div[1]/p[1]/text()")[1].strip('\n')
        location = div.xpath("./div/div/a[1]/div[1]/div[1]/span/text()")[0]
        print(title,price,company,location)
        file.write(f'{title},{price},{company},{location}\n')
    file.close()


def run(url):
    main_page = get_html(url)
    crawling_data(main_page)


# /html/body/div[6]/div/div/div[2]/div[5]/div[1]/div[1]/div/div/a[1]/div[1]/p
# //*[@id="utopia_widget_76"]/a[2]/div[2]/div[1]/span[1]
# /html/body/div[6]/div/div/div[2]/div[5]/div[1]/div[1]/div/div/a[2]/div[2]/div[1]/span[1]

if __name__ == '__main__':

    url_site = "https://chengdu.zbj.com/search/f/?type=new&kw=saas&r=2"
    run(url_site)
