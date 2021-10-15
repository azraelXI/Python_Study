from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
import time
web = Chrome()
web.get("http://lagou.com")
el = web.find_element_by_xpath('//*[@id="changeCityBox"]/p[1]/a')
el.click()
time.sleep(1)
web.find_element_by_xpath('//*[@id="search_input"]').send_keys('python', Keys.ENTER)
time.sleep(1)
web.find_element_by_xpath('//*[@id="s_position_list"]/ul/li[1]/div[1]/div[1]/div[1]/a/h3').click()
web.switch_to.window(web.window_handles[-1])    # 切换窗口
job_detail = web.find_element_by_xpath('//*[@id="job_detail"]/dd[2]/div').text
web.close()
web.switch_to.window(web.window_handles[0])     # 回到原来窗口
time.sleep(1)
li_list = web.find_elements_by_xpath('//*[@id="s_position_list"]/ul/li')
for li in li_list:
    job_name = li.find_element_by_tag_name('h3').text
    job_money = li.find_element_by_xpath('./div/div/div[2]/div/span').text
    company_name = li.find_element_by_xpath('./div/div[2]/div/a').text
    print(job_money, job_name, company_name)
web.switch_to.frame()
web.switch_to.default_content()
