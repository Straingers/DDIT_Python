import os
import sys
import urllib.request
from bs4 import BeautifulSoup
import pymysql

def insertChicken(datas):
    conn = pymysql.connect(host='localhost', user='root', password='java',
                           db='python', charset='utf8')
    curs = conn.cursor()
    sql = """
            insert into chicken(title, link, description, blogname, bloglink, postdata)
            values (%s, %s, %s, %s, %s, %s)
        """
    cnt = curs.executemany(sql, datas)
    conn.commit()
    conn.close()
    
    return cnt

client_id = "GKXLtdUCJZsxDI5ZqQJR"
client_secret = "MqOY5Vxi1l"
encText = urllib.parse.quote("치킨")
#url = "https://openapi.naver.com/v1/search/blog?query=" + encText # json 결과
url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()

if(rescode==200):
    response_body = response.read()
    
    html = response_body.decode('utf-8')
    soup = BeautifulSoup(html, 'xml')
    
    items = soup.select("item")
    datas = []
    for i, item in enumerate(items):
        data = (item.title.text
                , item.link.text
                , item.description.text
                , item.bloggername.text
                , item.bloggerlink.text
                , item.postdate.text
                )
        datas.append(data)
    cnt = insertChicken(datas)
    print("cnt", cnt)
else:
    print("Error Code:" + rescode)