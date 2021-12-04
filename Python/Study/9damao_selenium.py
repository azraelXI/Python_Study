from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from chaojiying import Chaojiying_Client
import random
import time
url_main = "http://www.9damaogame.com/forum-365-1.html"
url_task = "http://www.9damaogame.com/home.php?mod=task"
cjy = Chaojiying_Client('zxc1161929313', 'qq1161929313', '923487')
MessageList = ["Thank you!!!!! Thank you!!!!!", "Thanks for sharing!!", "Thanks for sharing!! Thanks!", "Thank you very much! Fierce!", "感谢分享！！！666", "牛逼啊 谢谢版主", "感谢分享！版主牛逼！"]
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36",
    "Cookie": "aU84_ef4f_saltkey=PaKOTOLP; aU84_ef4f_lastvisit=1632357670; aU84_ef4f_auth=3292cE0KVx5xi0vsIBLP07tz1fpCiv5XZHRYEy%2B%2Bbc%2FOn2z7Q61mCIApq9yprIuyjxgq4H%2FS6OjDJmdVG1%2FQm7zJ0a4f; aU84_ef4f_lastcheckfeed=1520685%7C1632361281; aU84_ef4f_connect_is_bind=0; aU84_ef4f_nofavfid=1; aU84_ef4f_smile=1D1; aU84_ef4f_taskdoing_1520685=1; aU84_ef4f_visitedfid=365D76D65D40; aU84_ef4f_st_t=1520685%7C1632797455%7Ccf6a31c1a31c04922c3034345c3c6368; aU84_ef4f_forum_lastvisit=D_76_1632706993D_365_1632797455; aU84_ef4f_viewid=tid_228065; aU84_ef4f_ulastactivity=1632798621%7C0; aU84_ef4f_sendmail=1; aU84_ef4f_noticeTitle=1; aU84_ef4f_st_p=1520685%7C1632798783%7Ccfda4d355f317a8342ade4565276c168; aU84_ef4f_checkpm=1; aU84_ef4f_lastrequest=74d2p%2FNBiAOKBvfOoS%2FWUJHkMnX18s%2BE7f59HGevB5wGRj6wzbUF; aU84_ef4f_lastact=1632798813%09forum.php%09ajax"
}
def SumAddAns():
    Sum = 0
    Question_text = web.find_element(By.XPATH, '/html/body/form/table/tbody/tr/td/table/tbody/tr/td/b')
    # 全部数字
    NumArray_String = Question_text.text.split(' + ')
    # print(NumArray_String)
    # 最后一位数字    NumArray_String[len(NumArray_String)-1].split(' ')[0]
    for num in range(len(NumArray_String) - 1):
        Sum += (int)(NumArray_String[num])
    Sum += (int)(NumArray_String[len(NumArray_String) - 1].split(' ')[0])
    # Sum为答案
    # 找到文本框输入答案 并点击进入
    Ans = web.find_element(By.XPATH, '/html/body/form/table/tbody/tr/td/table/tbody/tr/td/input[1]')
    Ans.send_keys(Sum)
    AnsBtn = web.find_element(By.XPATH, '/html/body/form/table/tbody/tr/td/table/tbody/tr/td/input[2]')
    AnsBtn.click()
    print("完成加法效验")
def Login():
    time.sleep(5)
    userNameText = web.find_element(By.XPATH, '/html/body/div[11]/div/div/div/div[2]/div/div[2]/div[1]/div[1]/form/div/div[1]/table/tbody/tr/td[1]/input')
    userPassText = web.find_element(By.XPATH, '/html/body/div[11]/div/div/div/div[2]/div/div[2]/div[1]/div[1]/form/div/div[2]/table/tbody/tr/td[1]/input')
    Code = web.find_element(By.XPATH, '/html/body/div[11]/div/div/div/div[2]/div/div[2]/div[1]/div[1]/form/div/span/div/table/tbody/tr/td/input')
    img = web.find_element(By.XPATH, '/html/body/div[11]/div/div/div/div[2]/div/div[2]/div[1]/div[1]/form/div/span/div/table/tbody/tr/td/span[2]/img').screenshot_as_png
    userNameText.send_keys('zxc1161929313')
    userPassText.send_keys('qq1161929313')
    verify = cjy.PostPic(img, 1902)
    verify_code = verify['pic_str']
    Code.clear()
    Code.send_keys(verify_code)
    LoginBtn = web.find_element(By.XPATH, '/html/body/div[11]/div/div/div/div[2]/div/div[2]/div[1]/div[1]/form/div/div[6]/table/tbody/tr/td[1]/button')
    LoginBtn.click()
    time.sleep(5)
    try:
        error = web.find_element(By.XPATH, '//*[@id="seccode_cS"]/div/table/tbody/tr/td/a').text
        if(error == "换一个"):
            cjy.ReportError(verify['pic_id'])
            print("验证码错误了")
            Login()
        else:
            print("完成登录")
    except:
        print("出现异常,完成登录")
def Task():
    for i in range(0, 3):
        web.get(url_task)
        try:
            TaskBtn = web.find_element(By.XPATH, "/html/body/div[10]/div/div/div[2]/div[1]/div/div/table/tbody/tr[3]/td[4]/a/img")
            TaskBtn.click()
            time.sleep(1)
            TaskBtn = web.find_element(By.XPATH,"/html/body/div[10]/div/div/div[2]/div[1]/div/div/table/tbody/tr[4]/td[4]/a/img")
            TaskBtn.click()
            time.sleep(1)
            TaskBtn = web.find_element(By.XPATH,"/html/body/div[10]/div/div/div[2]/div[1]/div/div/table/tbody/tr[5]/td[4]/a/img")
            TaskBtn.click()
            time.sleep(1)
        except:
            print("已经领取所有任务", i)
    print("领取任务完成")
def MainPage():
    for i in range(3, 80):
        web.get(url_main)
        time.sleep(2)
        if i > 40:
            ActionChains(web).key_down(Keys.END).key_up(Keys.END).perform()
        time.sleep(2)
        if i > 60:
            ActionChains(web).key_down(Keys.END).key_up(Keys.END).perform()
        time.sleep(3)
        try:
            elements = web.find_element(By.XPATH, f'/html/body/div[11]/div/div/div[4]/div/div/div[4]/div[2]/form/ul/li[{i}]')
            elements.click()
            time.sleep(3)
            ActionChains(web).key_down(Keys.END).key_up(Keys.END).perform()
            time.sleep(5)
            Textimput = web.find_element(By.XPATH, '/html/body/div[11]/div/div/div[4]/div[2]/div[1]/table/tbody/tr[1]/td[2]/div[2]/div/div[1]/form/div[1]/table/tbody/tr/td[2]/input')
            Textimput.clear()
            Textimput.send_keys(MessageList[random.randint(0, 6)])
            messBtn = web.find_element(By.XPATH, '/html/body/div[11]/div/div/div[4]/div[2]/div[1]/table/tbody/tr[1]/td[2]/div[2]/div/div[1]/form/div[1]/table/tbody/tr/td[4]/button')
            messBtn.click()
            time.sleep(2)
            print(i, "发送回复完成")
        except:
            print("加载页面太慢，重定位第二消息框")
            try:
                Textimput = web.find_element(By.XPATH, '/html/body/div[11]/div/div/div[4]/div[6]/form/table/tbody/tr/td[2]/div[1]/div[2]/div/div[1]/textarea')
                Textimput.send_keys(MessageList[random.randint(0, 6)])
                messBtn = web.find_element(By.XPATH, '/html/body/div[11]/div/div/div[4]/div[6]/form/table/tbody/tr/td[2]/p/button')
                messBtn.click()
                time.sleep(2)
                print(i, "发送回复完成")
            except:
                print("加载页面太慢，停止加载，继续下一步操作 此页面为：", i)
        print(i, "完成")
def Report(Url):
    web.get(Url)
    time.sleep(15)
    try:
        ActionChains(web).key_down(Keys.END).key_up(Keys.END).perform()
        time.sleep(2)
        Textimput = web.find_element(By.XPATH, '/html/body/div[11]/div/div/div[4]/div[2]/div[1]/table/tbody/tr[1]/td[2]/div[2]/div/div[1]/form/div[1]/table/tbody/tr/td[2]/input')
        Textimput.clear()
        Textimput.send_keys(MessageList[random.randint(0, 6)])
        messBtn = web.find_element(By.XPATH, '/html/body/div[11]/div/div/div[4]/div[2]/div[1]/table/tbody/tr[1]/td[2]/div[2]/div/div[1]/form/div[1]/table/tbody/tr/td[4]/button')
        messBtn.click()
        time.sleep(1)
        print("Report完成")
    except:
        print("加载页面太慢，停止加载，继续下一步操作")
        Report(Url)
def Access(Url):
    web.get(Url)
    time.sleep(3)
    Mainhandle = web.current_window_handle#主页面的句柄
    try:
        for id in range(2, 12):
            Player = web.find_element(By.XPATH, f'/html/body/div[11]/div/div/div[4]/div[2]/div[{id}]/table/tbody/tr[1]/td[1]/div/div[3]/div/a/img')
            Player.click()
            time.sleep(1)
        handles = web.window_handles
        for newhandle in handles:
            if(newhandle != Mainhandle):
                web.switch_to.window(newhandle)
                ActionChains(web).key_down(Keys.END).key_up(Keys.END).perform()
                acc = web.find_element(By.XPATH, '/html/body/div[6]/div/div/div[1]/div[1]/div[2]/div/ul/li[4]/a')
                acc.click()
                time.sleep(1)
                btn = web.find_element(By.XPATH, '/html/body/div[1]/div/table/tbody/tr[2]/td[2]/form/p/button')
                btn.click()
                web.close()
                print("打招呼完成")
    except:
        pass
    web.switch_to.window(Mainhandle)
    time.sleep(1)
if __name__ == '__main__':
    opt = Options()
    # opt.add_argument('--headless')
    web = Chrome(options=opt)
    web.get('http://www.9damaogame.com/member.php?mod=logging&action=login')
    time.sleep(2)
    SumAddAns()
    Login()
    # Task()
    Report("http://www.9damaogame.com/thread-155106-1-1.html")
    Report("http://www.9damaogame.com/thread-156809-1-1.html")
    Report("http://www.9damaogame.com/thread-231010-1-1.html")
    MainPage()
    Access("http://www.9damaogame.com/thread-155106-1-1.html")
    web.close()
    print("全部完成")
