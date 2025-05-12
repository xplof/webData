import requests
from bs4 import BeautifulSoup

url="https://finance.naver.com/sise/sise_market_sum.naver"
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"}
res=requests.get(url,headers=headers)
res.raise_for_status()#에러시 종료
soup=BeautifulSoup(res.text,"lxml")

data=soup.find("div",{"class":"box_type_l"})
trs=data.tbody.find_all("tr")
name=data.tbody.find_all("td",{"class":"title"})
for i in name:
   print(i.get_text())
