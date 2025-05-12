from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

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
url = "https://www.coupang.com"
broswer.get(url)

time.sleep(5)  # 페이지 로딩 대기

input("종료시 enter>> ")




# # 예시: 검색창에 '노트북' 입력
# search_input = driver.find_element(By.NAME, 'q')
# search_input.send_keys('노트북')
# search_input.submit()

# # 5초 대기 후 종료
# time.sleep(5)
# input("종료시 enter")
# driver.quit()