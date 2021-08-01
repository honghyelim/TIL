import requests
from bs4 import BeautifulSoup

url = 'https://search.daum.net/search?w=tot&DA=UME&t__nil_searchbox=suggest&sug=&sugo=15&sq=%EC%86%A1%ED%8C%8C+%ED%97%AC%EB%A6%AC&o=1&q=%EC%86%A1%ED%8C%8C+%ED%97%AC%EB%A6%AC%EC%98%A4%EC%8B%9C%ED%8B%B0'
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text,'lxml')

# with open('daum.html','w',encoding='utf8') as f:
#     f.write(soup.prettify())

data_rows = soup.find('table', attrs={'class':'tbl'}).find('tbody').find_all('tr')
for i, r in enumerate(data_rows):
    col = r.find_all('td')
    print("매물 {} :".format(i+1))
    print('거래 :', col[0].get_text())
    print('면적 :', col[1].get_text(), '(공급/전용)')
    print('가격 :',col[2].get_text(),'(만원')
    print('동 :',col[3].get_text())
    print('층 :',col[4].get_text())
