import requests
from bs4 import BeautifulSoup

# html파일을 읽어와서 html,css형태로 파싱
with open("w0509/게시판3.html","r",encoding="utf8") as f:
   soup=BeautifulSoup(f,"lxml")
   

#html태그 찾는 방법
print(soup.thead)
# soup.find("thead",{"class":""})
data=soup.find("thead")
ths=data.find_all("th")
for i in ths:
   print(i.get_text())

data=soup.find("div",{"id":"input"}).div
data2=data.find_next_sibling().find
print(data2)
for i in ths[0:5]:
   print(i.get_text())

# 자바스크립트를 읽을 수 없음. html문서만 가능 
data=soup.find("tbody",{"id":"tbody"})
trs=data.find_all("tr")
print(len(trs))
for i in trs:
   tds=i.find_all("td")
   if len(tds)>1: #td가 1개면 출력x
      for i in range(len(tds)-1): #01234
         print(tds[i].get_text(),end="\t")
      print()