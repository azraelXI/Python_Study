from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from chaojiying import Chaojiying_Client
import time

option = Options()
option.add_argument('--disable-blink-features=AutomationControlled')
web = Chrome(options=option)
web.get("https://www.12306.cn/index/")

web.find_element_by_xpath('//*[@id="J-btn-login"]').click()
web.find_element_by_xpath('//*[@id="toolbar_Div"]/div[2]/div[2]/ul/li[2]/a').click()
web.find_element_by_xpath('//*[@id="J-userName"]').send_keys('15625230921')
web.find_element_by_xpath('//*[@id="J-password"]').send_keys('qq1161929313')
web.find_element_by_xpath('//*[@id="J-login"]').click()
time.sleep(1)
btn = web.find_element_by_xpath('//*[@id="nc_1_n1z"]')
ActionChains(web).drag_and_drop_by_offset(btn, 300, 0).perform()
