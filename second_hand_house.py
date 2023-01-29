# -*- codeing = utf-8 -*-
# @Time: 2022/3/20 23:08
# @Author: Foxhuty
# @File: second_hand_house.py
# @Software: PyCharm
# @Based on python 3.10

from lxml import etree
import asyncio
import aiohttp
import aiofiles
import time
import pandas as pd

# url = "https://cd.58.com/ershoufang/p1/"

region_name = ''.join(input('请输入要查询的区域：').split('，'))


async def down_load(url, region_name):
    async with aiohttp.ClientSession() as session:
        async with await session.get(url=url, headers=headers) as response:
            response.get_encoding()
            page_text = await response.text()
            # print(page_text)
            tree = etree.HTML(page_text)
            # print(tree)
            divs = tree.xpath('//*[@id="__layout"]/div/section/section[3]/section[1]/section[2]/div')
            async with aiofiles.open(f"D:\\爬虫数据\\成都{region_name}区二手房价信息表.txt", mode='a', encoding='utf-8') as f:
                for div in divs:
                    region = div.xpath('./a/div[2]/div[1]/section/div[2]/p[2]/span[1]/text()')[0]
                    if region in region_name:
                        location = div.xpath('./a/div[2]/div[1]/section/div[2]/p[2]/span[2]/text()')[0]
                        address = div.xpath('./a/div[2]/div[1]/section/div[2]/p[2]/span[3]/text()')[0]
                        house = div.xpath('./a/div[2]//h3/text()')[0]
                        price = div.xpath('./a/div[2]/div[2]/p[1]/span/text()')
                        price = price[0] + "万元" if len(price) > 0 else ""
                        print(region, location, address, house, price)
                        await f.write(f'{region},\t{location},\t{address},\t{house},\t{price}\n')


async def main():
    tasks = []
    for page in range(1, 3):
        url = f"https://cd.58.com/ershoufang/p+{str(page)}/"
        tasks.append(asyncio.ensure_future(down_load(url=url, region_name=region_name)))
        print(f'开始爬取第{page}页数据')
        await asyncio.sleep(5)
        print(f'第{page}页完成')

    await asyncio.wait(tasks)


if __name__ == '__main__':
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36"
    }
    asyncio.run(main())
    file = f"D:\\爬虫数据\\成都{region_name}区二手房价信息表.txt"
    df_csv = pd.read_csv(file, sep=',\t', names=['城区名', '所在小区', '详细地址', '房屋描述', '售价'], engine='python')
    df_csv.to_excel(f'D:\\爬虫数据\\{region_name}.xlsx', index=False)
