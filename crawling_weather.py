# -*- codeing = utf-8 -*-
# @Time: 2022/4/20 21:34
# @Author: Foxhuty
# @File: crawling_weather.py
# @Software: PyCharm
# @Based on python 3.10
import requests
import time
import csv
from concurrent.futures import ThreadPoolExecutor


def get_data_json(url):
    page_json = requests.get(url, headers=headers, cookies=cookies).json()
    return page_json


def parse_data(url):
    file = open('weather_data.csv', mode='a', encoding='utf-8', newline='')
    csv_writer = csv.writer(file)
    page_json = get_data_json(url)
    for weather in page_json['data']['predict']['detail']:
        city = page_json['data']['predict']['station']['city']
        date = weather['date']
        info = weather['day']['weather']['info']
        temp = weather['day']['weather']['temperature']
        wind = weather['day']['wind']['power']
        wind_direct = weather['day']['wind']['direct']
        print(city, date, info, temp, wind, wind_direct)
        csv_writer.writerow([city, date, info, temp, wind, wind_direct])
    file.close()


def main(*province_name):
    region_url = "http://www.nmc.cn/rest/province/all?_=1650635275805"
    region_json = get_data_json(region_url)
    for region_code in region_json:
        region = region_code['code']
        province = region_code['name']
        # print(province)
        if province in province_name:
            url = f"http://www.nmc.cn/rest/province/{region}?_=1650444461514"
            code_json = get_data_json(url)
            print(f'==========正在爬取{province}天气数据==========')
            for code in code_json:
                code_number = code['code']
                url_location = f"http://www.nmc.cn/rest/weather?stationid={code_number}&_=1650444461512"
                parse_data(url_location)
            time.sleep(5)
        else:
            continue



if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
        'Referer': 'http://www.nmc.cn/',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive'
    }
    cookies = {
        "Cookie": "UM_distinctid=18045f807d5196-0798e00eb23f81-4e4c0f20-1fa400-18045f807d6385; __nmcu=1516686969298620416; __utrace=af19b265d6aa7df9474bf2b6e6f20552; ray_leech_token=1650441408; CNZZDATA1254743953=1643250002-1650437482-null%7C1650437504"
    }
    province = (input('输入要查询的省份：')).split('，')
    print(province)
    start = time.time()
    with ThreadPoolExecutor(50) as t:
        t.submit(main(*province))
    end = time.time()
    print(f'共计用时{end - start}')
