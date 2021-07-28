import os
import sys
import urllib.request
from bs4 import BeautifulSoup
import pymysql

def insertData(datas):
    conn = pymysql.connect(host='localhost', user='root', password='java',
                           db='python', charset='utf8')
    curs = conn.cursor()
    sql = """
            insert into stock(s_code, s_name, s_price, crawl_date)
            values (%s, %s, %s, %s)
        """
    cnt = curs.executemany(sql, datas)
    conn.commit()
    conn.close()
    
    return cnt

client_id = "GKXLtdUCJZsxDI5ZqQJR"
client_secret = "MqOY5Vxi1l"
#url = "https://openapi.naver.com/v1/search/blog?query=" + encText # json 결과
url = "https://vip.mk.co.kr/newSt/rate/item_all.php" # xml 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    
    html = response_body
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.select(".st2")
    datas = []
    for item in items:
        data = (
                item.parent.select_one("td:nth-of-type(1) > a").get("title")
                , item.text
                , item.parent.select_one("td:nth-of-type(2)").text.replace(",","")
                , "2020" + soup.select_one(".t_11_black").text.replace(".", "").replace(" ", ".").replace(":", "")
            )
        datas.append(data)
    cnt = insertData(datas)
    print("cnt", cnt)
else:
    print("Error Code:" + rescode)