import requests
from bs4 import BeautifulSoup
import csv

fileName = "list.csv"
ff = open("w0509/"+fileName,"w",encoding="utf-8-sig",newline="")
writer = csv.writer(ff)


with open('w0509/notice_list.html','r',encoding='utf8') as f:
   soup=BeautifulSoup(f,"lxml")
   
title=soup.find("table").find("tr").find_all('th')
#상단
toptitle = []
for i in title:
   print(i.get_text(),end="\t")
   toptitle.append(i.get_text())
writer.writerow(toptitle)
print()

#내용
trs=soup.find("table").find_all("tr")
for i in trs[1::2]:
   tds=i.find_all("td")
   body=[]
   for j in tds:
      print(j.get_text(),end="\t")
      body.append(j.get_text())
   writer.writerow(body)
   print()