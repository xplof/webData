import requests
from bs4 import BeautifulSoup

# url=("https://finance.naver.com/sise/sise_market_sum.naver")
url=("https://n.news.naver.com/article/011/0004483132?ntype=RANKING")
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"}
res=requests.get(url,headers=headers)
res.raise_for_status()

#문자열 -> html,css파싱
soup=BeautifulSoup(res.text,"lxml")
# print(soup)#html,css
# <title>태그에 접근해서 가져옴
print(soup.title)
print(soup.title.get_text()) #태그 안 텍스트형태로 출력
# 태그 속성을 출력
print(soup.header.div.a.attrs) #속성전체출력
print(soup.header.div.a['class']) #지정 속성 출력

# id, class 속성 출력
# find() 해당태그의 속성값으로 검색가능
data1=soup.find("a",{"class":"ofhd_float_back"})
print(data1)
data1=soup.find("a",class_="ofhd_float_back")
print(data1)

data2 = soup.find("h2",attrs={"id":"title_area"})
data2 = soup.find("h2",{"id":"title_area"})
print(data2.get_text())

# find() 1개만 검색, find_all() 복수개 검색
uldata=soup.find("ul",{"class":"ranking_list"})
# lidata=uldata.find("li",{"class":"rl_item"})
lidata=uldata.find_all("li",{"class":"rl_item"})
print(len(lidata))
print(lidata)

for s in lidata:
   print(s.find("p",{"class":"rl_txt"}).get_text())
