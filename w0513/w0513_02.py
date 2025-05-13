import requests
from bs4 import BeautifulSoup

# fly불러오기
# 항공사, 출발시간, 도착시간, 금액
with open("w0513/fly1.html",'r',encoding='utf8') as f:
   soup=BeautifulSoup(f,'lxml')

data=soup.find("body").find_all("div")
for i in data:
   imgs = i.find_all("img")
   for img in imgs:
      airline_name = img.get("alt")  # 또는 img["alt"]
      if airline_name:  # alt 속성이 있는 경우에만 출력
         print(airline_name)

time=soup.find("body").find_all("b",{'class','route_time__xWu7a'})
print(time)



