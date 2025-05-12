import requests
from bs4 import BeautifulSoup
import csv

with open('w0509/join02_info_input.html','r',encoding='utf8') as f:
   soup=BeautifulSoup(f,"lxml")

#파일저장
ff=open('w0509/input.csv','w',encoding='utf-8-sig',newline='')
writer=csv.writer(ff)

dls=soup.find_all("fieldset")
File=[]
for i in dls:
   dts=i.find_all("dt")
   for j in dts:
      print(j.get_text().strip(),end=" ") #공백제거 strip()
      File.append(j.get_text().strip())
writer.writerow(File)
ff.close()