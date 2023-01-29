# -*- codeing = utf-8 -*-
# @Time: 2022/3/16 21:25
# @Author: Foxhuty
# @File: thread_test_001.py
# @Software: PyCharm
# @Based on python 3.10

from threading import Thread

class MyThread(Thread):
    def run(self):
        for i in range(1000):
            print(f'子线程：{i}')


if __name__ == '__main__':
    t=MyThread()
    t.start()
    for i in range(1000):
        print(f'主线程：{i}')
