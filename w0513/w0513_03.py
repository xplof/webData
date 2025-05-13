import requests
from bs4 import BeautifulSoup
### fly1.html 불러오기
## 항공사, 출발시간,도착시간, 금액
with open("w0513/fly1.html","r",encoding="utf-8") as f:
   soup = BeautifulSoup(f,"lxml")
datas = soup.find_all("div",{"class":"domestic_Flight__8bR_b"})
print(len(datas))
d_list = []
for data in datas:
   airline = data.find("b",{"class":"airline_name__0Tw5w"}).get_text().strip()
   print(airline)
   times = data.find_all("b",{"class":"route_time__xWu7a"})
   startTime = times[0].get_text().strip()
   print(startTime)
   endTime = times[1].get_text().strip()
   print(endTime)
   price = data.find("i",{"class":"domestic_num__ShOub"}).get_text().strip().replace(",","")
   price = int(price)
   print(price)
   print('-'*50)
   d_list.append([airline,startTime,endTime,price])
### list 정렬
dd_list = sorted(d_list,key = lambda x:x[3]) # 순차정렬
# dd_list = sorted(d_list,key = lambda x:x[3], reverse=True ) # 역순정렬
print(dd_list)