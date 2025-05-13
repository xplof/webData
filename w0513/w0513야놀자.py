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

url="https://nol.yanolja.com/"
browser.get(url)
time.sleep(3)


elem=browser.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div[2]/div/div[1]/a[1]/div/span[1]/img')
elem.click()
time.sleep(1)

elem=browser.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div/div[1]/div/div/button/span')
elem.click()
time.sleep(1)

elem=browser.find_element(By.XPATH,'//*[@id="_MODAL_DIM_"]/div/section/div[2]/div[1]/button[3]')
elem.click()
time.sleep(1)

elem=browser.find_element(By.XPATH,'//*[@id="_MODAL_DIM_"]/div/section/div[2]/div[2]/div/div/button[2]')
elem.click()
time.sleep(1)

input("s")



# 호텔/리조트 클릭
# 지역선택 > 제주 > 서귀포시
# 6/7~6/8 적용하기 버튼 클릭
# 스크롤 내리기
# 호텔, 호텔명, 평점, 후기개수, 가격