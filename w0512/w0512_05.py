import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import csv
import time
# 셀레니움 크롬자동화 프로그램
# user-agent 변경
options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=1920x1080")
options.add_argument('User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64),\
   Accept-Language: ko-KR,ko;q=0.9,Referer: https://www.coupang.com/')
# options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",\
#                      "Accept-Language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7')
browser = webdriver.Chrome(options=options)
browser.maximize_window()
url = "https://www.melon.com/chart/index.htm"
browser.get(url)
time.sleep(3) #페이지 로딩 대기
soup=BeautifulSoup(browser.page_source,'lxml')
data=soup.find("tbody")
trs=data.find_all("tr")
tds=trs[0].find_all("td")
# print(tds[1].get_text())
# print(tds[6].get_text())
# print(tds[7].get_text())
print(tds[3].img['src'])
imgUrl=tds[3].img['src']
img_res= requests.get(imgUrl)
with open("w0512/melon_chart1.jpg",'wb') as f:
   f.write(img_res.content)
for index, td in enumerate(tds):
   if index in [1, 6, 7]:
      print(td.get_text(strip=True), end=" ")

input("종료시 enter")
# 셀레니움 크롬자동화 프로그램
# browser = webdriver.Chrome()
# browser.get("https://www.whatismybrowser.com/detect/what-is-my-user-agent")

