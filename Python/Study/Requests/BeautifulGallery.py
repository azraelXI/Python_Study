import csv
import requests
import time
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
url = f"https://umei.cc/meinvtupian/meinvxiezhen/index_{id}.htm"
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36"
}

# for i in range(1, 150):
#     url = f"https://umei.cc/meinvtupian/meinvxiezhen/index_{i}.htm"
#     resp = requests.get(url=url, headers=headers)
#     resp.encoding = "utf-8"
#     main_page = BeautifulSoup(resp.text, "html.parser")
#     try:
#         alist = main_page.find("div", class_="TypeList").find_all("a")
#         domin = 'https://umei.cc'
#     except:
#         print(url)
#     else:
#         for a in alist:
#             href = a.get('href')
#             child_url = domin + href
#             child_page_resp = requests.get(child_url)
#             child_page_resp.encoding = "utf-8"
#             child_page_content = child_page_resp.text
#             child_page = BeautifulSoup(child_page_content, "html.parser")
#
#             div = child_page.find("div", class_="ImageBody")
#             img = div.find("img")
#             src = img.get('src')
#
#             img_resp = requests.get(src)
#             img_name = src.split("/")[-1]
#             with open("img/"+img_name, mode='wb') as f:
#                 f.write(img_resp.content)
#             child_page_resp.close()
#             print("Over!!", img_name)
#             time.sleep(1)
#         print(url, "OVER!")
#         resp.close()
# print("OverAll!")

def download_one_Page(url):
    resp = requests.get(url=url, headers=headers)
    resp.encoding = "utf-8"
    main_page = BeautifulSoup(resp.text, "html.parser")
    try:
        alist = main_page.find("div", class_="TypeList").find_all("a")
        domin = 'https://umei.cc'
    except:
        print(url)
    else:
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
            with open("img/" + img_name, mode='wb') as f:
                f.write(img_resp.content)
            child_page_resp.close()
            time.sleep(1)
        print(url, "提取完毕")
    resp.close()

if __name__ == '__main__':
    with ThreadPoolExecutor(50) as t:
        for i in range(1, 151):
            t.submit(download_one_Page, f"https://umei.cc/meinvtupian/meinvxiezhen/index_{i}.htm")
    print("全部提取完毕")
