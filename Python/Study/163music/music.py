import requests
import time
import lxml
import json
from Crypto.Cipher import AES
from base64 import b64encode

url = "https://music.163.com/weapi/comment/resource/comments/get?csrf_token="
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36",
    "cookie": "_iuqxldmzr_=32; _ntes_nnid=ebccf1d438138f09619cc5f52a0bf55f,1632803176079; _ntes_nuid=ebccf1d438138f09619cc5f52a0bf55f; NMTID=00OHaxgt1oHnNry8U6ttth03BKnC74AAAF8KqdADg; WM_TID=PTLcMIC7%2BohBAQURAFNv4Q3MzG9kUaN4; WNMCID=urtmmk.1632803176716.01.0; WEVNSM=1.0.0; NTES_P_UTID=0MqovS0RdxpXvRGCcgBBJnsJxtgu3wVj|1632980157; P_INFO=xiyang15625230921@163.com|1632980157|0|mail163|00&99|anh&1632064786&d90_client#gud&440300#10#0#0|156921&0|mail163|xiyang15625230921@163.com; WM_NI=yTxoGtq%2FPrYuO3gPksORXTRoNW0U9EKCF0w6u%2BBVzeQEHFsSXqZ%2Fd7SGep88nMxlvmb%2B3mK1Q8ESDfGvuAWt6rFIPXG87fjz4DFRebutCNy%2FIY8snlsy5U%2FSU7uKvOJncUo%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eebafb63a79ffa8bc25dac8e8fa2d84b869e9eaef17c88bef7b0f46df2be9ba7d42af0fea7c3b92abb8cb890c680b3f1a093dc7f8deda9b1ea798d8e98b5d1658e8900b6bc4f899d8ad1f63eb7f58eb7f96f939b88a7f2599caf96d0e73d9199ab91bb34ae93b88df567a2f5fd8eca3b93e88bb4c76e85aabba2d680f6ae8aaad35485e8f987e972f89c8ab3e86ab7ac8daffc258b87f894ed68b1a7fbb6ae5997e9bbacf5458ab2adb6ee37e2a3; playerid=35048532; JSESSIONID-WYYY=fWvGeP13O1UAvQKXm2P%2Fs4leVt0fNVfIy%2FaHpr3E3AednRnv4nAWBOycY9HOUEVn4x2gIwGgIeWOsfd5GVrgd%5CZuEotdO9zWwIXQB2H32aBK3DESgk352U%2BpghC6MQxXJjO0FucYb%5CrSjMGZgf2oe%2F52N7BXCfm%2BXS1BDn6hMxdn8bNi%3A1633680014006"
}
data = {
    "csrf_token": "",
    "cursor": "-1",
    "offset": "0",
    "orderType": "1",
    "pageNo": "1",
    "pageSize": "20",
    "rid": "R_SO_4_1880886636",
    "threadId": "R_SO_4_1880886636"
}
f = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
g = '0CoJUm6Qyw8W8jud'
e = '010001'
i = "qzRLapEcuSKDDCjj"

def get_encSecKey():
    return "0962be5e110332350ccc812f07b695028b7777006c9b818e6ea33e5a6d57e726df84b186422882b5487727e33da794b5df2dda44e50bcf818633e74c4b18401fe3ddd369ac327856bf7d25b159d7d97cd3c093abdc4ebad2505d0b06ebc85fb910c64385572888758decc8f5949c220d1112d70fe5270db0ffdc4155f421b2cd"
def get_params(data):
    first = enc_params(data, g)
    params = enc_params(first, i)
    return params
def to_16(data):
    pad = 16 - len(data) % 16
    data += chr(pad) * pad
    return data
def enc_params(data,key):
    iv = '0102030405060708'
    data = to_16(data)
    aes = AES.new(key=key.encode('utf-8'), iv=iv.encode('utf-8'), mode=AES.MODE_CBC)
    bs = aes.encrypt(data.encode('utf-8'))
    return str(b64encode(bs), 'utf-8')
"""
function a(a) {
        var d, e, b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", c = "";
        for (d = 0; a > d; d += 1)
            e = Math.random() * b.length,
            e = Math.floor(e),
            c += b.charAt(e);
        return c
    }
    function b(a, b) {
        var c = CryptoJS.enc.Utf8.parse(b)
          , d = CryptoJS.enc.Utf8.parse("0102030405060708")
          , e = CryptoJS.enc.Utf8.parse(a)
          , f = CryptoJS.AES.encrypt(e, c, {
            iv: d,
            mode: CryptoJS.mode.CBC
        });
        return f.toString()
    }
    function c(a, b, c) {
        var d, e;
        return setMaxDigits(131),
        d = new RSAKeyPair(b,"",c),
        e = encryptedString(d, a)
    }
    function d(d, e, f, g) { d=data e=010001 
        var h = {}
          , i = a(16);
        return h.encText = b(d, g),
        h.encText = b(h.encText, i),
        h.encSecKey = c(i, e, f),
        h
    }
"""

resp = requests.post(url, data={
    "params": get_params(json.dumps(data)),
    "encSecKey": get_encSecKey()
}, headers=headers)
print(resp.text)
resp.close()