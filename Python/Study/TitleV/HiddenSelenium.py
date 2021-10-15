from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
opt = Options()
opt.add_argument('--headless')
opt.add_argument('--disable-gpu')
web = Chrome(options=opt)
web.get("https://www.endata.com.cn/BoxOffice/BO/Year/index.html")
sel_el = web.find_element_by_xpath('//*[@id="OptionDate"]')
sel = Select(sel_el)    #下拉框
for i in range(len(sel.options)):
    sel.select_by_index(i)
    time.sleep(2)
    print(web.find_element_by_xpath('//*[@id="TableList"]/table').text)
web.close()