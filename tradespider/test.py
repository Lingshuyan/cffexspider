# -*- coding = utf-8 -*-
# @Time : 2021/3/7
# @File : test.py
# @Software : PyCharm
import datetime

start_date=datetime.datetime.strptime('2021-03-06', '%Y-%m-%d')
now_date=datetime.datetime.now()
days_delta = int((now_date - start_date).days)+1

for i in range(0,days_delta):
    delta = datetime.timedelta(days=i)
    year_month = (start_date + delta).strftime('%Y%m')
    days = (start_date + delta).strftime('%d')
    html = "http://www.cffex.com.cn/sj/ccpm/%s/%s/IF.xml?"%(year_month,days)
    print(html)

# print(start_date)
# print(now_date)
# print(days_delta)