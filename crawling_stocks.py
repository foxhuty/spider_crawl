# -*- codeing = utf-8 -*-
# @Time: 2022/4/20 23:50
# @Author: Foxhuty
# @File: crawling_stocks.py
# @Software: PyCharm
# @Based on python 3.10
import requests
import csv

with open(r'D:\爬虫数据\stocks_short.csv', mode='a', encoding='utf-8', newline='') as file_data:
    csv_writer = csv.DictWriter(file_data, fieldnames=['股票代码', '股票名称', '当前价格', '涨跌额', '涨跌幅', '年初至今',
                                                       '成交量', '成交额', '换手率', '市盈率(TTM)', '股息率', '市值'])
    csv_writer.writeheader()

    for page in range(1, 5):
        url = f"https://xueqiu.com/service/v5/stock/screener/quote/list?page={page}&size=30&order=desc&order_by=amount&exchange=CN&market=CN&type=sha&_=1650469926246"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
        }
        response = requests.get(url, headers=headers)
        response.encoding = 'utf-8'
        page_json = response.json()

        for data in page_json['data']['list']:
            # print(data['name'])
            symbol = data['symbol']
            name = data['name']
            price = data['current']
            chg = data['chg']
            if chg:
                if float(chg) > 0:
                    chg = '+' + str(chg)
                else:
                    chg = str(chg)
            percent = data['percent']
            if percent:
                if float(percent) > 0:
                    percent = '+' + str(percent) + '%'
                else:
                    percent = str(percent) + '%'
            current_year_percent = str(data['current_year_percent']) + '%'
            volume = data['volume']
            amount = data['amount']
            turn_over = str(data['turnover_rate']) + '%'
            pe_ttm = data['pe_ttm']
            dividend = data['dividend_yield']
            if dividend:
                dividend = str(dividend) + '%'
            else:
                dividend = None
            market_capital = data['market_capital']
            data_dict = {
                '股票代码': symbol,
                '股票名称': name,
                '当前价格': price,
                '涨跌额': chg,
                '涨跌幅': percent,
                '年初至今': current_year_percent,
                '成交量': volume,
                '成交额': amount,
                '换手率': turn_over,
                '市盈率(TTM)': pe_ttm,
                '股息率': dividend,
                '市值': market_capital
            }
            csv_writer.writerow(data_dict)
            print(symbol, name, price, chg, percent, current_year_percent, volume, amount, turn_over, pe_ttm, dividend,
                  market_capital)
