import requests
import asyncio
import aiohttp
import aiofiles
from Crypto.Cipher import AES
import re
import os

re =re.compile(r"")
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36",
    "Cookie" : "aU84_ef4f_saltkey=PaKOTOLP; aU84_ef4f_lastvisit=1632357670; aU84_ef4f_auth=3292cE0KVx5xi0vsIBLP07tz1fpCiv5XZHRYEy%2B%2Bbc%2FOn2z7Q61mCIApq9yprIuyjxgq4H%2FS6OjDJmdVG1%2FQm7zJ0a4f; aU84_ef4f_lastcheckfeed=1520685%7C1632361281; aU84_ef4f_connect_is_bind=0; aU84_ef4f_nofavfid=1; aU84_ef4f_smile=1D1; aU84_ef4f_taskdoing_1520685=1; aU84_ef4f_visitedfid=365D76D65D40; aU84_ef4f_st_t=1520685%7C1632797455%7Ccf6a31c1a31c04922c3034345c3c6368; aU84_ef4f_forum_lastvisit=D_76_1632706993D_365_1632797455; aU84_ef4f_viewid=tid_228065; aU84_ef4f_ulastactivity=1632798621%7C0; aU84_ef4f_sendmail=1; aU84_ef4f_noticeTitle=1; aU84_ef4f_st_p=1520685%7C1632798783%7Ccfda4d355f317a8342ade4565276c168; aU84_ef4f_checkpm=1; aU84_ef4f_lastrequest=74d2p%2FNBiAOKBvfOoS%2FWUJHkMnX18s%2BE7f59HGevB5wGRj6wzbUF; aU84_ef4f_lastact=1632798813%09forum.php%09ajax"
}

url = "https://18.mediayun.xyz/videos/202110/26/6176e5c86820e1239a994d7d/bd92ga/index.m3u8"

resp = requests.get(url, headers)
m3u8 = resp.text     #m3u8


resp.close()
