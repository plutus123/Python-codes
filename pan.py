import requests
from bs4 import BeautifulSoup
all_url=['http://books.toscrape.com/page-1.html']
current_page='http://books.toscrape.com/catalogue/page-1.html'
base_url='http://books.toscrape.com/catalogue/'
response = requests.get(current_page)
while response.status_code==200:
    data=BeautifulSoup(response.text,'html.parser')
    next_page=data.find(class_='next')
    if next_page is None:
        break
    next_page_url=base_url+next_page.a['href']
    print(next_page_url)
    all_url.append(next_page_url)
    current_page=next_page_url
    response=requests.get(current_page)