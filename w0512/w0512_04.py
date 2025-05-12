import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import csv
import time

#셀레니움 크롬자동화 프로그램
browser=webdriver.Chrome()
browser.get("https://www.naver.com")

elem =browser.find_element(By.ID,"query") #query선택
elem.send_keys("시가 총액")                #시가총액 글자입력
elem.send_keys(Keys.ENTER)                #enter키 입력

time.sleep(2) #2초동안 멈춤

elem=browser.find_element(By.XPATH,'//*[@id="main_pack"]/section[2]/div/ul/li[2]/div/div[2]/div[1]/a')
elem.click() #해당위치 클릭
time.sleep(1)
browser.switch_to.window(browser.window_handles[0]) #첫번째 탭 활성화
browser.back() #뒤로가기
time.sleep(1)
browser.refresh() #새로고침
time.sleep(1)
browser.forward()

input("키보드 클릭")


