import requests
from bs4 import BeautifulSoup
import csv

# 파일저장
fileName="board.csv"
ff = open("w0509/"+fileName,"w",encoding="utf-8-sig",newline="")
writer= csv.writer(ff)

toptitle=[]
with open("w0509/게시판3.html","r",encoding="utf8")as f:
   soup=BeautifulSoup(f,'lxml')

# 상단제목 파일에 저장
menu=soup.find("thead").find("tr").find_all("th")
for i in menu:
   print(i.get_text(),end="\t")
   toptitle.append(i.get_text())
print()
writer.writerow(toptitle)

# 몸통부분 파일에 저장

trs=soup.find("tbody").find_all("tr")
for i in trs: 
   tds=i.find_all("td")
   if len(tds)>1:
      for i in tds[0:5]:
         print(i.get_text(),end="\t")
         
      print()
      