import requests
import asyncio
import aiohttp
import aiofiles
from Crypto.Cipher import AES
import re
import os
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36"
}
# 抓取视频
# 1.找到m3u8文件
# 2.通过m3u8文件下载ts文件
# 3.将ts文件合并为一个mp4文件
obj = re.compile(r'var now="(?P<url>.*?)";', re.S)    # m3u8地址
def getm3u8(url):
    resp = requests.get(url, headers)
    resp.encoding = 'utf-8'
    page_text = resp.text
    m3u8_url = obj.findall(page_text)[0]
    resp.close()
    resp2 = requests.get(m3u8_url, headers)
    url_main = "https://v4.cdtlas.com/"
    m3u8_url2 = url_main + resp2.text.split('?User-Agent')[0].split('/', 1)[1]
    resp2.close()
    resp3 = requests.get(m3u8_url2, headers)
    with open("video/哲仁王后_m3u8.txt", mode='wb') as f:
        f.write(resp3.content)
    resp3.close()
async def download_ts(url, name, session):
    async with session.get(url) as resp:
        async with aiofiles.open(f"video/{name}", mode='wb') as f:
            await f.write(await resp.content.read())
    print(f"{name}下载完毕")
async def aio_download():
    tasks = []
    async with aiohttp.ClientSession() as session:
        async with aiofiles.open("video/哲仁王后_m3u8.txt", mode='r', encoding='utf-8') as f:
            async for line in f:
                if line.startswith("#"):
                    continue
                line = line.strip()
                name = line.rsplit('/', 1)[1]
                task = asyncio.create_task(download_ts(line, name, session))
                tasks.append(task)
            await asyncio.wait(tasks)
def getkey(url):
    resp = requests.get(url)
    resp.encoding = 'utf-8'
    return resp.text
async def dec_ts(name, key):
    aes_new = AES.new(key=key, IV=b"0000000000000000", mode=AES.MODE_CBC)
    async with aiofiles.open(f"video/{name}", mode='rb') as f1,\
        aiofiles.open(f"video/temp_{name}", mode='wb') as f2:
        bs = await f1.read()
        await f2.write(aes_new.decrypt(bs))
    print(f"{name}完毕")
async def aio_dex(key):
    tasks = []
    async with aiofiles.open("video/哲仁王后_m3u8.txt", mode='r', encoding='utf-8') as f:
        async for line in f:
            if line.startswith("#"):
                continue
            line = line.strip()
            task = asyncio.create_task(dec_ts(line, key))
            tasks.append(task)
        await asyncio.wait(tasks)
    pass
def merge_ts():
    lst = []
    with open("video/哲仁王后_m3u8.txt", mode='r', encoding='utf-8') as f:
        for line in f:
            if line.startswith("#"):
                continue
            line = line.strip()
            lst.append(f"video/{line}")
    s = "".join(lst)
    os.system(f"copy /b {s} movie.mp4")
    print("搞定")
if __name__ == '__main__':
    # url = "https://www.91mjw.cc/video/1666-0-0.html"
    # getm3u8(url)  #下载m3u8文件
    # asyncio.run(aio_download())   #下载ts视频
    """
    key_url = "https://hey07.789zy.cc/20211011/kKmy98Af/1200kb/hls/key.key"
    key = getkey(key_url)
    asyncio.run(aio_dex(key))
    """
    merge_ts()
    pass