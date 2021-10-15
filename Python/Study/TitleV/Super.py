from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from chaojiying import Chaojiying_Client
import time
option = Options()
option.add_argument('--disable-blink-features=AutomationControlled')
web = Chrome(options=option)
web.get("http://www.chaojiying.com/")

web.find_element_by_xpath('//*[@id="carousel-example-generic"]/div/div[1]/article/a[2]').click()

img = web.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/form/div/img').screenshot_as_png
cjy = Chaojiying_Client('zxc1161929313', 'qq1161929313', '923487')
verify_code = cjy.PostPic(img, 1902)['pic_str']

web.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/form/p[1]/input').send_keys("zxc1161929313")

web.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/form/p[2]/input').send_keys("qq1161929313")

web.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/form/p[3]/input').send_keys(verify_code)

web.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/form/p[4]/input').click()