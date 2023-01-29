# -*- codeing = utf-8 -*-
# @Time: 2022/3/14 1:06
# @Author: Foxhuty
# @File: crawling_ts_video.py
# @Software: PyCharm
# @Based on python 3.10

import requests
import asyncio
import aiohttp
import aiofiles
from Crypto.Cipher import AES


def get_content(m3u8_src, file_name=None):
    response = requests.get(m3u8_src)
    # print(response.status_code)
    with open(file_name, mode='wb') as f:
        f.write(response.content)


def main(url):
    get_content(url, file_name=r'./video_downloads/girls_ts.txt')
    # downloads_ts(file_name=r'./video_downloads/video_ts.txt')


def get_key(url):
    resp = requests.get(url)
    # print(resp.text)
    return resp.text


async def ts_dec(name, key):
    aes = AES.new(key=key, IV=b"0000000000000000", mode=AES.MODE_CBC)
    async with aiofiles.open(f'./video_downloads/ts_downloaded/{name}', mode='rb') as f1, \
            aiofiles.open(f'./video_downloads/ts_downloaded/temp_{name}', mode='wb') as f2:
        bs = await f1.read()
        await f2.write(aes.decrypt(bs))
    print(f'{name}处理完成。。。')


async def aio_dec(key):
    tasks = []
    async with aiofiles.open('./video_downloads/girls_ts.txt', mode='r', encoding='utf-8') as f:
        async for line in f:
            if line.startswith('#'):
                continue
            else:
                line = line.strip()
                name = line.split('/')[5]
                task = asyncio.create_task(ts_dec(name, key))
                tasks.append(task)
        await asyncio.wait(tasks)


async def download_ts(url, name, session):
    async with session.get(url) as response:
        async with aiofiles.open(f'./video_downloads/ts_downloaded/{name}', mode='wb') as f:
            await f.write(await response.content.read())
    print(f'{name}下载完毕')


async def aio_download():
    tasks = []
    async with aiohttp.ClientSession() as session:
        async with aiofiles.open('./video_downloads/girls_ts.txt', mode='r', encoding='utf-8') as f:
            async for line in f:
                # line = line.strip()
                if line.startswith('#'):
                    continue
                else:
                    line = line.strip()
                    # "https://vod1.ttbfp2.com"
                    up_url = f'https://vod1.ttbfp2.com{line}'
                    name = line.split('/')[5]
                    task = asyncio.create_task(download_ts(up_url, name, session))
                    tasks.append(task)
            await asyncio.wait(tasks)


if __name__ == '__main__':
    url_ts = 'https://vod1.ttbfp2.com/20210803/1FPRurBM/375kb/hls/index.m3u8?auth_key=1654341013-0-0-1a13e3c4c346bda473996699dd846658'
    # main(url)
    key_url = "https://vod1.ttbfp2.com/20210803/1FPRurBM/375kb/hls/key.key"

    # get_content('https://vod1.ttbfp2.com/20210911/OzGnmGDv/2000kb/hls/SxxfMKDR.ts','./video_downloads/1.ts')
    loop = asyncio.get_event_loop_policy().get_event_loop()
    # loop.run_until_complete(aio_download())
    key = get_key(key_url)
    # key = "7f983555dcf9bbe9"
    loop.run_until_complete(aio_dec(key))
