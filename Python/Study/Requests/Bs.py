import csv
import requests
import bs4

url = "http://www.xinfadi.com.cn/getPriceData.html"
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36"
}
f = open("../data.csv", mode="a", encoding="utf-8")
_writer = csv.writer(f)

resp = requests.post(url=url, headers=headers)
page_content = resp.json()
#print(page_content)
for it in page_content['list']:
    print("品名:" + it['prodName'] + "最低价" + it['lowPrice'] + "平均价" + it['avgPrice'] + "最高价" + it['highPrice'] + "发布日期" + it['pubDate'])

resp.close()