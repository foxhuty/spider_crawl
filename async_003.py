# -*- codeing = utf-8 -*-
# @Time: 2022/3/20 1:47
# @Author: Foxhuty
# @File: async_003.py
# @Software: PyCharm
# @Based on python 3.10
import asyncio


async def request(url):
    print('request a url', url)
    await asyncio.sleep(2)
    print('request finished successfully', url)


# urls = [
#     "http://kr.shanghai-jiuxin.com/file/2020/0807/98ec5c7f5d7d0b2d750dd9b5ea834cfc.jpg",
#     "http://kr.shanghai-jiuxin.com/file/2020/1031/a2c58d6d726fb7ef29390becac5d8643.jpg",
#     "http://kr.shanghai-jiuxin.com/file/2020/1031/774218be86d832f359637ab120eba52d.jpg",
#     "http://kr.shanghai-jiuxin.com/file/2020/0717/ee96dff8bd3297a1062b4d23f79bbc6b.jpg",
#     "http://kr.shanghai-jiuxin.com/file/2020/1031/e9d17d27dfd693d88b232899538144e8.jpg",
#     "http://kr.shanghai-jiuxin.com/file/2022/0316/0deb28f71fc8f6b835f94a26c3eb6ae9.jpg",
#     "http://kr.shanghai-jiuxin.com/file/2022/0316/843e214fea6978a133bdad04b5706120.jpg",
#     "http://kr.shanghai-jiuxin.com/file/2022/0316/ea3ce3f2e0f9a0f0e8f081ada58ae7d4.jpg",
#     "http://kr.shanghai-jiuxin.com/file/2022/0316/5f9f5694d47fa502164e39a46b01a9a1.jpg",
#     "https://wx1.sinaimg.cn/large/005zeEDvgy1gh4re3pud8j30u01900zw.jpg",
#     "https://img3.027art.cn/img/2021/08/10/1628536655727570.jpg"
# ]
# tasks = []
# for url in urls:
#     page = request(url)
#     task = asyncio.ensure_future(page)
#     tasks.append(task)
#
# loop = asyncio.get_event_loop()
# 需要将任务列表封装到wait中
# loop.run_until_complete(asyncio.wait(tasks))
async def main():
    urls = [
        "http://kr.shanghai-jiuxin.com/file/2020/0807/98ec5c7f5d7d0b2d750dd9b5ea834cfc.jpg",
        "http://kr.shanghai-jiuxin.com/file/2020/1031/a2c58d6d726fb7ef29390becac5d8643.jpg",
        "http://kr.shanghai-jiuxin.com/file/2020/1031/774218be86d832f359637ab120eba52d.jpg",
        "http://kr.shanghai-jiuxin.com/file/2020/0717/ee96dff8bd3297a1062b4d23f79bbc6b.jpg",
        "http://kr.shanghai-jiuxin.com/file/2020/1031/e9d17d27dfd693d88b232899538144e8.jpg",
        "http://kr.shanghai-jiuxin.com/file/2022/0316/0deb28f71fc8f6b835f94a26c3eb6ae9.jpg",
        "http://kr.shanghai-jiuxin.com/file/2022/0316/843e214fea6978a133bdad04b5706120.jpg",
        "http://kr.shanghai-jiuxin.com/file/2022/0316/ea3ce3f2e0f9a0f0e8f081ada58ae7d4.jpg",
        "http://kr.shanghai-jiuxin.com/file/2022/0316/5f9f5694d47fa502164e39a46b01a9a1.jpg",
        "https://wx1.sinaimg.cn/large/005zeEDvgy1gh4re3pud8j30u01900zw.jpg",
        "https://img3.027art.cn/img/2021/08/10/1628536655727570.jpg"
    ]
    tasks = [asyncio.create_task(request(url)) for url in urls]
    # for url in urls:
    #     tasks.append(asyncio.create_task(request(url)))
    await asyncio.wait(tasks)


if __name__ == '__main__':
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(main())
    asyncio.run(main())
