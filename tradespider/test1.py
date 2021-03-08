# -*- coding = utf-8 -*-
# @Time : 2021/3/7
# @File : test1.py
# @Software : PyCharm

import urllib.request

def askURL(url):
    response = urllib.request.urlopen(url)
    html = response.read().decode('utf-8')
    return html

url = "http://www.cffex.com.cn/sj/ccpm/202103/05/IF.xml?"
html = askURL(url)
print(html)