import requests
from bs4 import BeautifulSoup

url = 'http://localhost/CRAWL/crawl.html'

response = requests.get(url)

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    tds = soup.select("td")
    for i, td in enumerate(tds):
        if i > 1:
            print(td.get_text())

else : 
    print(response.status_code)