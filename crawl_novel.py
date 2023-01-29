# -*- codeing = utf-8 -*-
# @Time: 2022/6/11 13:41
# @Author: Foxhuty
# @File: crawl_novel.py
# @Software: PyCharm
# @Based on python 3.10
# from config import MAIL_PASS
from imbox import Imbox
import datetime

mail_host = 'smtp.qq.com'
# mail_pass = 'dgfzajxvpltkbghb'
mail_pass = 'gdhprdriyijibjfi'

sender = '80708055@qq.com'

with Imbox(mail_host, username=sender, password=mail_pass, ssl=True) as imbox:
    all_inbox_messages = imbox.messages(date__gt=datetime.date(2022, 1, 1))
    for uid,message in all_inbox_messages:
        # print(uid,message)
        # imbox.mark_seen(uid)
        if message.attachments:
            print(message.attachments)
        print(message.sent_from)
        if message.subject:
            print(message.subject)
        print('='*50)
