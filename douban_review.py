# -*- codeing = utf-8 -*-
# @Time: 2022/3/13 17:47
# @Author: Foxhuty
# @File: douban_review.py
# @Software: PyCharm
# @Based on python 3.10
import requests
from lxml import etree
from tqdm import tqdm
import time

url = "https://movie.douban.com/subject/35148918/reviews?start=%d"

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': 'll="118318"; bid=U-JINgcxlHs; __utmz=30149280.1644911731.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _vwo_uuid_v2=DA2A95E1866E924E6C0D9C884B602F68D|ceadbc1b76ad62c752b3a08b5727d75a; ct=y; __gads=ID=7db67329d3653670-228271dcecd0004a:T=1647061308:RT=1647061308:S=ALNI_MaRCvxVjs9tIUYEMGeu2qnYSO-2AQ; __utma=30149280.776264061.1644911731.1647068230.1647168577.5; __utmc=30149280; __utmt=1; dbcl2="237418054:e0Lrln4/tsI"; ck=mMjl; push_noty_num=0; push_doumail_num=0; __utmv=30149280.23741; __utmb=30149280.3.10.1647168577; __utma=223695111.940450960.1644911733.1647068231.1647168605.5; __utmb=223695111.0.10.1647168605; __utmc=223695111; __utmz=223695111.1647168605.5.3.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1647168605%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _pk_ses.100001.4cf6=*; _pk_id.100001.4cf6=42176308bb1d3ed0.1644911733.5.1647168623.1647069783.',
    'Host': 'movie.douban.com',
    'Referer': 'https://movie.douban.com/subject/35148918/reviews?start=20',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'}

if __name__ == '__main__':
    for i in range(6):
        movie_url = url % (i * 20)
        response = requests.get(movie_url, headers=headers)
        response.encoding = 'utf-8'

        page_code = response.text
        # with open(r'D:\成绩统计结果\movie_review.html',mode='w',encoding='utf-8') as f:
        #     f.write(page_code)
        html = etree.HTML(page_code)
        comments = html.xpath('//*[ @ id = "content"]/div/div[1]/div[1]/div')
        # '// *[ @ id = "content"] / div / div[1] / div[1]'
        f=open(r'D:\成绩统计结果\movie_review.csv', mode='a+', encoding='utf-8')
        # f.write(f'作者\t标题\t评论\t日期\n')
        for comment in comments:
            author = comment.xpath('./div/header/a[2]/text()')[0]

            title = comment.xpath('./div/div/h2/a/text()')[0]
            review = comment.xpath('./div/div/div/div/text()')[0].strip(' \n').split('(')[0]
            print(review)
            # review_date = comment.xpath('./div/header/span[2]/@content')
            review_date = comment.xpath('./div/header/span[2]/text()')
            f.write(f'{author},{title},{review},{review_date}')
        # print(f'第{i+1}页保存完成。。。')
        time.sleep(1)
        f.close()

