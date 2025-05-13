import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import csv
import time
import random
# 크롬 옵션 설정 - 셀레니움 접근 제한 : 보안접근 해제
options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")  # 자동화 티 안 나게
options.add_argument("start-maximized")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
# 브라우저 실행
browser = webdriver.Chrome(options=options)
browser.maximize_window() #창 최대화

### 네이버 자동 로그인 메일 쓰기
url = "https://flight.naver.com/"
browser.get(url)
time.sleep(2) # 페이지 로딩 대기

elem=browser.find_element(By.XPATH,'//*[@id="layer"]/button[1]')
elem.click()
select=browser.find_element(By.CLASS_NAME,"select_code__IVa3P")
select.click()
time.sleep(1)
elem=browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[8]/div[2]/div/div/ul[1]/li[2]/button')
elem.click()
elem=browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[2]/div/div/div[2]/div[1]/button[2]/b')
elem.click()
elem=browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[8]/div[1]/div/input')
elem.send_keys("이탈리아")
elem.send_keys(Keys.ENTER)
time.sleep(2)
elem=browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[8]/div[2]/section/ul/li[1]/a')
elem.click()
# 항공권클릭
elem=browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[2]/div/div/div[2]/button/span')
elem.click()
time.sleep(2)
elem=browser.find_element(By.XPATH,'//*[@id="__next"]/div/div/main/article/div[2]/div/div[2]/div[5]/button[1]/div')
elem.click()
time.sleep(2)
elem=browser.find_element(By.XPATH,'//*[@id="__next"]/div/div/div[2]/div[2]/div[1]/div[2]/ul/li[2]/a')
elem.click()
time.sleep(15)
# 스크롤내리기
# 현재 사이트 높이를 가져오는 자바스크립트
scroll=browser.execute_script("return document.body.scrollHeight")


# 웹스크래핑
soup=BeautifulSoup(browser.page_source,'lxml')
with open("w0513/fly1.html",'w',encoding='utf-8-sig',newline='') as f:
   f.write(soup.prettify())
print("파일저장 완료")

input("press any key")
