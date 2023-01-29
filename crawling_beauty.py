# -*- codeing = utf-8 -*-
# @Time: 2022/5/10 22:51
# @Author: Foxhuty
# @File: crawling_beauty.py
# @Software: PyCharm
# @Based on python 3.10
import asyncio
import aiohttp
import aiofiles
from lxml import etree
import os


dirName = r'D:\爬虫数据\beauty_2'
if not os.path.exists(dirName):
    os.mkdir(dirName)


async def parse_specific_image_group(url):
    async with aiohttp.ClientSession(headers=headers) as session:
        async with await session.get(url) as response:
            # response.get_encoding()
            page_html = await response.text()
            if response.status != 404:
                tree = etree.HTML(page_html)
                image_src = tree.xpath('//div[@class="content-box"]/section/a/img/@src')[0]
                image_name = image_src.split('/')[-1]
                image_path = dirName + '/' + image_name
                async with await session.get(image_src) as response_image:
                    image_data = await response_image.content.read()
                    async with aiofiles.open(image_path, 'wb') as f:
                        await f.write(image_data)
                        print(f'{image_name}爬取完成')


async def run():
    tasks = [asyncio.create_task(parse_specific_image_group(url))]
    url_head = url.split('.')[0:-1]
    url_head = '.'.join(url_head)
    for i in range(2, 50):
        url_specific = f'{url_head}_{i}.htm'
        tasks.append(asyncio.create_task(parse_specific_image_group(url_specific)))
        await asyncio.wait(tasks)
        # await asyncio.sleep(5)


if __name__ == '__main__':
    url = "https://www.umei.cc/meinvtupian/xingganmeinv/8743.htm"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36",
        "Referer": "https://www.umeitu.com/meinvtupian/xingganmeinv/"
    }
    # asyncio.run(run())
    # loop = asyncio.get_event_loop_policy().get_event_loop()

    # loop.run_until_complete(run())
    asyncio.run(run())
