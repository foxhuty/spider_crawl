# -*- codeing = utf-8 -*-
# @Time: 2022/2/28 2:50
# @Author: Foxhuty
# @File: crawler_5.py
# @Software: PyCharm
# @Based on python 3.10
import re

s = """
<div class='jay'><span id='1'>网站妹子</span></div>
<div class='tom'><span id='2'>人世间</span></div>
<div class='min'><span id='3'>假日喜洋洋（2）</span></div>
<div class='real'><span id='4'>陈钰琪</span></div>
<div class='luck'><span id='5'>倚天屠龙记</span></div>
<div class='fancy'><span id='6'>Great Gates</span></div>
<div class='great'><span id='7'>2024年高考</span></div>
"""

obj = re.compile(r"<div class='.*?'><span id='\d+'>(?P<event>.*?)</span>", re.S)

result=obj.finditer(s)
for it in result:
    print(it.group('event'))

re=obj.findall(s)

print(re)