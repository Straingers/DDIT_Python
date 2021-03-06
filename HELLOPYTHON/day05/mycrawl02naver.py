import os
import sys
import urllib.request
import requests
from bs4 import BeautifulSoup

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
    soup = BeautifulSoup(html, 'html.parser')
    
    items = soup.select("item")
    for i, item in enumerate(items):
        print(item.title.text)
        print(item.description.text + "\n\n")
else:
    print("Error Code:" + rescode)