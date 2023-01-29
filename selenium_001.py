# -*- codeing = utf-8 -*-
# @Time: 2022/3/20 3:24
# @Author: Foxhuty
# @File: selenium_001.py
# @Software: PyCharm
# @Based on python 3.10
from selenium import webdriver
from lxml import etree
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

brower = webdriver.Chrome()
brower.get('http://lagou.com')
el = brower.find_element(by=By.XPATH, value='//*[@id="changeCityBox"]/p[1]/a')
el.click()
time.sleep(2)
brower.find_element(by=By.XPATH, value='//*[@id="search_input"]').send_keys('python', Keys.ENTER)

div_list = brower.find_elements(by=By.XPATH, value='//*[@id="jobList"]/div[1]/div')

for div in div_list:
    job_name = div.find_element(by=By.XPATH, value='./div[1]/div[1]/div[1]/a').text
    salary = div.find_element(by=By.XPATH, value='./div[1]/div[1]/div[2]/span').text
    company = div.find_element(by=By.XPATH, value='./div/div[2]/div/a').text
    print(company, job_name, salary)
    # time.sleep(5)
brower.find_element(by=By.XPATH, value='//*[@id="jobList"]/div[1]/div[1]/div[1]/div[1]/div[1]/a').click()
brower.switch_to.window(brower.window_handles[-1])
job_detail = brower.find_element(by=By.XPATH, value='//*[@id="job_detail"]').text
print(job_detail)
time.sleep(5)
brower.close()
brower.switch_to.window(brower.window_handles[0])
