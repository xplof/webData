# 1. 네이버 접속
# 2. 검색창 시가총액 입력
# 3. 엔터키 입력
# 4. 삼성전자 클릭이동

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import csv
import time

# 크롬 옵션 설정 - 셀레니움 접근 제한 : 보안접근 해제
options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")  # 자동화 티 안 나게
options.add_argument("start-maximized")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

# 브라우저 실행
browser = webdriver.Chrome(options=options)

### 네이버 자동 로그인 메일 쓰기
url = "https://www.naver.com/"
browser.get(url)
time.sleep(2) # 페이지 로딩 대기

select=browser.find_element(By.ID,'query')
select.send_keys("시가총액")
select.send_keys(Keys.ENTER)





input("df")