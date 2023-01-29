# -*- codeing = utf-8 -*-
# @Time: 2022/2/14 21:01
# @Author: Foxhuty
# @File: crawler_1.py
# @Software: PyCharm
# @Based on python 3.10

import requests
import re
import json
import pprint


url = "https://search.51job.com/list/000000,000000,0000,00,9,99,python,2,1.html"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"
}
response = requests.get(url, headers=headers)
# response.encoding = 'GBK'
html_text = response.text

# print(html_text)
re_obj = re.compile('window.__SEARCH_RESULT__ = (.*?)</script>', re.S)
html_json = re_obj.findall(html_text)[0]

# print(html_json)
html_dict=json.loads(html_json)
print(html_dict)



for data in html_dict:
    title=data['job_name']
    print(title)
    pprint.pprint(data)
