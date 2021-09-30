import csv
import requests
import re
index = 0

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36"
}
obj = re.compile( r'<li>.*?<span class="title">(?P<Name>.*?)</span>.*?<p class="">(?P<Director>.*?)&nbsp.*?<span class="inq">(?P<Quotes>.*?)</span>', re.S)

for j in range(10):
    url = f"https://movie.douban.com/top250?start={index}&filter="
    resp = requests.get(url=url, headers=headers) #请求HTML
    page_content = resp.text
    #print(url)
    f = open("../data.csv", mode="a", encoding="utf-8")
    _writer = csv.writer(f)
    it = obj.finditer(page_content)
    for i in it:
        dic = i.groupdict()
        dic["Director"] = dic["Director"].strip()
        _writer.writerow((dic.values()))
    resp.close()
    index += 25
print("Over!")
