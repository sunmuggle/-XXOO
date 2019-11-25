import os
import requests
from bs4 import BeautifulSoup
#if __name__ == '__name__':
urlnext = 'http://jandan.net/ooxx'

for b in range(82,90):
 re = requests.get(urlnext)
 soup = BeautifulSoup(re.text,"html.parser")
 href = soup.find_all(class_='view_img_link')
 url_next = soup.find(title = 'Older Comments')
 urlnext = "http:"+url_next.get('href')
#with open('抓取.txt','wb+') as f:
 #f.write(href)
 print("下载第", b ,"页",)
 try:
   os.makedirs('./图片/图片'+format(b))
   print("创建成功")
 except:
   print("文件夹已存在")
 i = 0
 for a in href:
   #print(a.get('href'))
   url = 'http:'+ a.get('href')
   img = requests.get(url = url)
   i = i+1
   with open('./图片/图片'+format(b)+'/'+format(i) + '.jpg','wb+') as f:
      f.write(img.content)