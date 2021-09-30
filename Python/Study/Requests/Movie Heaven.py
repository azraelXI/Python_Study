import requests
import re
import csv

url = "https://www.dytt8.net/"
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36"
}

resp = requests.get(url=url, headers=headers)
resp.encoding = 'gb2312'
page_content = resp.text
#print(page_content)

obj1 = re.compile(r"2021新片精品.*?<ul>(?P<ul>.*?)</ul>", re.S)
obj2 = re.compile(r"<a href='(?P<href>.*?)'", re.S)

result1 = obj1.finditer(page_content)
ul = result1.__next__().group('ul')
result2 = obj2.finditer(ul)

child_href_list = []
for it in result2:
    child_href = url + it.group('href').strip("/")
    child_href_list.append(child_href)
resp.close()

obj3 = re.compile(r'◎译　　名　(?P<Name>.*?)<br />.*?target="_blank" href="(?P<DowloadUrl>.*?)">')
f = open("../data.csv", mode="a", encoding="utf-8")
_writer = csv.writer(f)
for i in child_href_list:
    child_resp = requests.get(url=i, headers=headers)
    child_resp.encoding = 'gb2312'
    child_page_content = child_resp.text
    result3 = obj3.finditer(child_page_content)
    for it in result3:
        dic = it.groupdict()
        dic["Name"] = dic["Name"].strip()
        dic["DowloadUrl"] = dic["DowloadUrl"].strip()
        _writer.writerow((dic.values()))
    child_resp.close()
print("OVER!")