# -*- coding = utf-8 -*-
# @Time : 2021/3/7
# @File : cffexspider.py
# @Software : PyCharm

# -*- coding = utf-8 -*-
# @Time : 2021/3/7
# @File : cffexspider.py
# @Software : PyCharm

import urllib.request
from bs4 import BeautifulSoup     #网页解析，获取数据
import re      #正则表达式，进行文字匹配
import datetime
import xlwt

# response = urllib.request.urlopen("http://www.cffex.com.cn/sj/ccpm/202103/05/IF.xml?")
# print(response.read().decode('utf-8'))

def main():
    # 1.爬取网页
    datalist = getData()
    savepath = "2021.xls"

    # 3.保存数据
    saveData(datalist,savepath)
    #askURL("https://movie.douban.com/top250?start=0")






#得到指定一个URL的网页内容
def askURL(url):
    request = urllib.request.Request(url)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode('utf-8')
        #print(html)
    except UnicodeDecodeError as result:
        pass
    return html

#合约类型
findInstrumentid = re.compile(r'<instrumentid>(.*?)</instrumentid>')         #创建正则表达式对象，表示规则（字符串的模式）
# 排名类型 value=0 成交量 value=1 持买单量 value=2 持卖单量
findRanktype = re.compile(r'<datatypeid>(.*?)</datatypeid>')
#排名
findRank = re.compile(r'<rank>(.*?)</rank>')
#公司
findShortname = re.compile(r'<shortname>(.*?)</shortname>')
#成交量
findVolume = re.compile(r'<volume>(.*?)</volume>')
#比上交易日增减
findVarvolume = re.compile(r'<varvolume>(.*?)</varvolume>')

#爬取网页
def getData():
    datalist = []

    # 设置爬取日期
    # 开始爬取日期
    start_date = datetime.datetime.strptime('2021-01-01', '%Y-%m-%d')
    # 结束日期 一般为今天
    now_date = datetime.datetime.strptime('2021-03-07', '%Y-%m-%d')
    # now_date = datetime.datetime.now()
    days_delta = int((now_date - start_date).days) + 1
    for i in range(0, days_delta):
        delta = datetime.timedelta(days=i)
        year_month = (start_date + delta).strftime('%Y%m')
        days = (start_date + delta).strftime('%d')
        year_month_days = (start_date + delta).strftime('%Y%m%d')
        url = "http://www.cffex.com.cn/sj/ccpm/%s/%s/IF.xml?" % (year_month, days)
        html = askURL(url)  #保存获取到的网页源码
        # 2.解析数据
        soup = BeautifulSoup(html,"html.parser")
        for item in soup.find_all('data'):  #查找符合要求的字符串形成列表
             data = []                      #保存交易的全部信息
             item = str(item)

             # 交易日期
             Trade_date = year_month_days
             data.append(Trade_date)

             # 合约id
             Instrumentid = re.findall(findInstrumentid,item)[0]  #re库用来通过正则表达式查找指定的字符串
             data.append(Instrumentid)                       #添加合约类型

             # 排名类型
             Ranktype =  re.findall(findRanktype,item)[0]
             data.append(Ranktype)

             # 排名
             Rank = re.findall(findRank, item)[0]
             data.append(Rank)

             # 公司名
             Shortname = re.findall(findShortname, item)[0]
             data.append(Shortname)

             #成交量
             Volume = re.findall(findVolume, item)[0]
             data.append(Volume)

             # 比上交易日增减
             Varvolume = re.findall(findVarvolume, item)[0]
             data.append(Varvolume)


             datalist.append(data)   #把处理好的一部电影信息放入datalist
        #
        #
        #
        print(datalist)


    return datalist


# 保存数据
def saveData(datalist,savepath):
    print("save....")
    book = xlwt.Workbook(encoding="utf-8")  # 创建workbook对象
    sheet = book.add_sheet('交易数据',cell_overwrite_ok=True)  #创建工作表
    col = ("交易日期","合约id","排名类型","排名","公司名","成交量","比上交易日增减")
    for i in range(0,7):
        sheet.write(0,i,col[i]) #列名

    i = 1
    for data in datalist:
        for j in range(0,len(data)):
            sheet.write(i,j,data[j]) #数据
        i += 1
    book.save(savepath)

if __name__ == "__main__":     #当程序执行时
    # 调用函数
    main()

