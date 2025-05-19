# 크롬 옵션 설정 - 셀레니움 접근 제한 : 보안접근 해제
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
from datetime import datetime
standard_time=datetime(2025,5,31,17,00,00)
now_time=datetime(2025,5,31,15,00,34)


url="https://www.yeogi.com/?utm_source=google_PC&utm_medium=sa&utm_campaign=240823_GC_UA_PC_AW_SA&utm_content=BRD_GN_001&utm_term=%EC%97%AC%EA%B8%B0%EC%96%B4%EB%95%8C&gad_source=1"
options=Options()
options.add_argument

browser=webdriver.Chrome(options=options)
# browser.maximize_window()
# browser.get(url)
# time.sleep(2)

soup=BeautifulSoup(browser.page_source,'lxml')
# #해외숙소 선택
# e=browser.find_element(By.XPATH,'//*[@id="LARGE_TAB_OVERSEAS_ACCOMMODATION"]/span')
# e.click()
# e=browser.find_element(By.XPATH,'//*[@id="__next"]/main/section[1]/div/div/div[2]/form/div[1]/div[1]/div/label/div/div[2]/input')
# e.send_keys("오사카")
# time.sleep(1)
# e=browser.find_element(By.XPATH,'//*[@id="__next"]/main/section[1]/div/div/div[2]/form/div[1]/div[2]/ul/li[1]')
# e.click()
# time.sleep(2)

# # 날짜선택
# e=browser.find_element(By.XPATH,'//*[@id="__next"]/main/section[1]/div/div/div[2]/form/div[2]/div[2]/div/div[1]/div[1]/button[2]')
# e.click()
# time.sleep(1)
# e.click()
# e=browser.find_element(By.XPATH,'//*[@id="__next"]/main/section[1]/div/div/div[2]/form/div[2]/div[2]/div/div[1]/div[2]/div[2]/div/div/ul[2]/li[26]/button/span')
# e.click()
# e=browser.find_element(By.XPATH,'//*[@id="__next"]/main/section[1]/div/div/div[2]/form/div[2]/div[2]/div/div[1]/div[2]/div[2]/div/div/ul[2]/li[28]/button/span')
# e.click()
# e=browser.find_element(By.XPATH,'//*[@id="__next"]/main/section[1]/div/div/div[2]/form/div[4]/button/span')
# e.click()
# input("sd")
score=soup.find("div",{"class":"css-19f645y"}).find_all("span",{"class":"css-9ml4lz"})
for i in score:
   print(i)