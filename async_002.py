# -*- codeing = utf-8 -*-
# @Time: 2022/3/20 0:50
# @Author: Foxhuty
# @File: async_002.py
# @Software: PyCharm
# @Based on python 3.10

import asyncio
import time


async def request(url):
    print('request a url', url)
    # time.sleep(2)
    await asyncio.sleep(2)
    print('request finished successfully', url)
    return url


page = request('www.foxhuty.com')


def callback_func(task):
    print(task)
    print('here it is')


if __name__ == '__main__':
    # ______________________________________
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(result)
    # ——————————————————————————————————————
    # 关于task
    # loop=asyncio.get_event_loop()
    # task=loop.create_task(result)
    # print(task)
    # loop.run_until_complete(task)
    # print(task)
    # ——————————————————————————————————————————
    # 关于future
    # loop=asyncio.get_event_loop()
    # task=asyncio.ensure_future(page)
    # print(task)
    # loop.run_until_complete(task)
    # print(task)
    # 关于回调函数
    loop = asyncio.get_event_loop()
    task = loop.create_task(page)
    task.add_done_callback(callback_func)
    loop.run_until_complete(task)
