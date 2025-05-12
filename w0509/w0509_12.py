import requests
from bs4 import BeautifulSoup
import csv

url=("https://finance.naver.com/sise/sise_market_sum.naver")
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"}
res=requests.get(url,headers=headers)
res.raise_for_status() #에러시종료
soup=BeautifulSoup(res.text,'lxml')

print(soup.thead)
ff=open("w0509/stock.csv",'w',encoding='utf-8-sig',newline='')
writer=csv.writer(ff)
ths=soup.thead.find_all("th")

fileName=[]
for th in ths:
   print(th.get_text(),end=' ')
   fileName.append(th.get_text())
writer.writerow(fileName)
ff.close()
print("파일저장완")

trs=soup.find("tbody").find_all("tr")
for i in trs:
   tds=i.find_all("td")
   for j in tds:
      print(j.get_text(separator="", strip=True), end='  ')
   print()