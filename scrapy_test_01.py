# -*- codeing = utf-8 -*-
# @Time: 2022/3/24 20:50
# @Author: Foxhuty
# @File: scrapy_test_01.py
# @Software: PyCharm
# @Based on python 3.10
import scrapy
import pandas as pd

file = r'D:\爬虫数据\成都成华金牛区二手房价信息表.txt'
# df=pd.read_csv('weather_data.csv')
# print(df.head())
# df.to_excel(r'D:\爬虫数据\weather_data.xlsx',index=False)

df_csv = pd.read_csv(file, header=None,sep=',\t')

print(df_csv)
# df_csv.to_excel(r'D:\爬虫数据\成都二手房1111.xlsx', index=False)
