import requests

# 쿠팡 접근해서 res.text출력
# res=requests.get("https://www.coupang.com/")
# res=requests.get("https://www.daum.net/")
# url=("https://www.whatismybrowser.com/detect/what-is-my-user-agent/")
# url=("https://www.melon.com/")
url=("https://www.google.com/")
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"}
res=requests.get(url,headers=headers)
res.raise_for_status()
print(res.text)
with open("w0509/test.html","w",encoding="utf8") as f:
   f.write(res.text)
print("응답코드 : ",res.status_code)