from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import csv
from bs4 import BeautifulSoup

# 크롬 옵션 설정
options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")  # 자동화 티 안 나게
options.add_argument("start-maximized")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

# 브라우저 실행
broswer = webdriver.Chrome(options=options)

# 쿠팡 페이지 접속
url = "https://www.melon.com/chart/index.htm"
broswer.get(url)

# time.sleep(5)  # 페이지 로딩 대기

soup=BeautifulSoup(broswer.page_source,'lxml')

# 타이틀
title=['순위','곡제목','가수','좋아요']
# 파일저장
ff=open("w0512/melon1.csv","a",encoding='utf-8-sig',newline="")
writer=csv.writer(ff)
writer.writerow(title)

trs=soup.find("tbody").find_all("tr")
for i in trs:
   cont=[]
   tds=i.find_all("td")
   for j,v in enumerate(tds):
      if j in [1]:
         print(v.get_text(strip=True),end="  ")
         cont.append(v.get_text(strip=True))
      elif j in [5]:
         print(v.find_all("a")[0].get_text(strip=True),end="  ")
         print(v.find_all("a")[1].get_text(strip=True),end="  ")
         cont.append(v.find_all("a")[0].get_text(strip=True))
         cont.append(v.find_all("a")[1].get_text(strip=True))
      elif j in [7]:
         # cnt = tds[7].find("span",{"class":"cnt"}).get_text().strip()[3:].strip() #총건수 함수제거보다 슬라이싱이 더 빠름
         print(v.find("span",{"class":"cnt"}).get_text(strip=True).replace("총건수",","),end="  ")
         cont.append(v.get_text(strip=True))
      # elif j in [3]:
      #    print(v.img["src"],end="  ")
   print()
   writer.writerow(cont)
ff.close()
# 1~100등
# 순위 곡정보 가수 좋아요 이미지링크
# 1 너에게닿기를 10cm 32412 http://
# 합계 : 좋아요 총개수










input("종료시 enter>> ")




# # 예시: 검색창에 '노트북' 입력
# search_input = driver.find_element(By.NAME, 'q')
# search_input.send_keys('노트북')
# search_input.submit()

# # 5초 대기 후 종료
# time.sleep(5)
# input("종료시 enter")
# driver.quit()