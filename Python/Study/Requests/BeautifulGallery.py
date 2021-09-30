import csv
import requests
import time
from bs4 import BeautifulSoup

url = "https://umei.cc/meinvtupian/meinvxiezhen"
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36"
}

resp = requests.get(url=url, headers=headers)
resp.encoding = "utf-8"
#print(resp.text)
main_page = BeautifulSoup(resp.text, "html.parser")

alist = main_page.find("div", class_="TypeList").find_all("a")
domin = 'https://umei.cc'
for a in alist:
    href = a.get('href')
    child_url = domin + href
    child_page_resp = requests.get(child_url)
    child_page_resp.encoding = "utf-8"
    child_page_content = child_page_resp.text
    child_page = BeautifulSoup(child_page_content, "html.parser")

    div = child_page.find("div", class_="ImageBody")
    img = div.find("img")
    src = img.get('src')

    img_resp = requests.get(src)
    img_name = src.split("/")[-1]
    with open("img/"+img_name, mode='wb') as f:
        f.write(img_resp.content)
    child_page_resp.close()
    print("Over!!", img_name)
    time.sleep(1)
print("OverAll!")
resp.close()