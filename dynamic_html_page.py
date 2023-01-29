# -*- codeing = utf-8 -*-
# @Time: 2022/3/20 17:27
# @Author: Foxhuty
# @File: dynamic_html_page.py
# @Software: PyCharm
# @Based on python 3.10

import requests
import asyncio
import aiohttp
import aiofiles


# url = "http://www.xinfadi.com.cn/getPriceData.html"


async def get_page(url, data):
    async with aiohttp.ClientSession() as session:
        async with session.post(url=url, data=data, headers=headers) as response:
            response.get_encoding()
            dic_json = await response.json()
            async with aiofiles.open("D:\\爬虫数据\\北京新发地菜价1111.txt", mode='a', encoding='utf-8') as f:
                for item in dic_json['list']:
                    name_id = item['id']
                    name = item['prodName'].replace('/', '')
                    price = item['avgPrice']
                    location = item['place']
                    print(name_id, name, price, location)
                    await f.write(f'{name_id},\t{name},\t{price},\t{location}\n')


async def download_all_page(url):
    tasks = []
    for page in range(1, 501):
        data = {
            "limit": 20,
            "current": page}
        tasks.append(asyncio.ensure_future(get_page(url=url, data=data)))
        # print(f'第{page}页爬取完成。。。。')
    await asyncio.wait(tasks)


if __name__ == '__main__':
    url_page = "http://www.xinfadi.com.cn/getPriceData.html"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36"
    }
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(download_all_page())
    asyncio.run(download_all_page(url_page))
