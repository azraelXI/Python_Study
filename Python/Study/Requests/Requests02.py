import requests

url="https://fanyi.baidu.com/sug"
dic={
    "kw":"dog"
}
resp=requests.post(url,data=dic)
print(resp.json())
resp.close()