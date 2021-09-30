import requests
url='http://www.baidu.com/s?wd=bilibili'

headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36"
}

resp=requests.get(url,headers=headers)
print(resp)
print(resp.text)
resp.close()
