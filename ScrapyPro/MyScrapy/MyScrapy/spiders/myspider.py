import scrapy
from ScrapyPro.MyScrapy.MyScrapy.items import MyscrapyItem


class MyspiderSpider(scrapy.Spider):
    # 爬虫文件名称：爬虫源文件的唯一标识
    name = 'myspider'
    # 允许的域名:用来限定start_urls列表中哪些url可以进行请求发送。一般不用，常被注释掉
    # allowed_domains = ['www.xxx.com']
    # 起始的url列表：列表中的url会被scrapy自动进行请求
    start_urls = ['https://fang.5i5j.com/bj/loupan/']

    def parse(self, response,**kwargs):
        h_list = response.css("li.houst_ctn")
        for vo in h_list:
            item = MyscrapyItem()
            item['title'] = vo.css("span.house_name::text").extract_first()
            item['location'] = vo.re_first(r'data-address="(.*?)" data-propertytypename=').strip()
            item['price'] = vo.css("p.price::text").extract_first()
            print(item)
