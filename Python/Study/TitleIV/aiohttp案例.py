import requests
import asyncio
import aiohttp
import aiofiles
import json
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36"
}
async def aiodownload(cid, b_id, title):
    data = {
        'book_id': b_id,
        'cid': f'{b_id}|{cid}',
        'need_bookinfo': 1
    }
    data = json.dumps(data)
    url = f"http://dushu.baidu.com/api/pc/getChapterContent?data={data}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            dic = await resp.json()
            async with aiofiles.open("novel/"+title, mode="w", encoding='utf-8') as f:
                await f.write(dic['data']['novel']['content'])
async def getCatalog(url):
    resp = requests.get(url)
    items = resp.json()['data']['novel']['items']
    tasks = []
    for item in items:
        title = item['title']
        cid = item['cid']
        tasks.append(asyncio.create_task(aiodownload(cid, b_id, title)))
    await asyncio.wait(tasks)

if __name__ == '__main__':
    b_id = [
        '4306063500'
    ]
    for id in b_id:
        url = 'http://dushu.baidu.com/api/pc/getCatalog?data={"book_id":"'+ id +'"}'
        asyncio.run(getCatalog(url))

