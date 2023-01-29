# -*- codeing = utf-8 -*-
# @Time: 2022/3/21 22:27
# @Author: Foxhuty
# @File: selenium_002.py
# @Software: PyCharm
# @Based on python 3.10

from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


web = Chrome()
web.get('https://lagou.com')

# el = web.find_element_by_xpath('//*[@id="changeCityBox"]/p[1]/a')
# el=web.find_element(value='//*[@id="changeCityBox"]/p[1]/a')
el = web.find_element(By.XPATH, value='//*[@id="changeCityBox"]/p[1]/a')
el.click()
time.sleep(2)

web.find_element(By.XPATH, value='//*[@id="search_input"]').send_keys('python', Keys.ENTER)


web.close()
