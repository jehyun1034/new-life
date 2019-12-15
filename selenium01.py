# gmail에 자동으로 들어가서 메일을 보내기 
from selenium import webdriver

from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.action_chains import ActionChains 
 
import time 

driver = webdriver.Chrome() 
url = 'https://google.com'
driver.get(url)
action = ActionChains(driver)

driver.find_element_by_css_selector('#gb_70').click()

action.send_keys('jehyun1034').perform()

driver.find_element_by_css_selector(".RveJvd.snByac").click()

time.sleep(2)
driver.find_element_by_css_selector(".whsOnd.zHQkBf").send_keys('#a1034817')
driver.find_element_by_css_selector(".RveJvd.snByac").click()
# 위에 까지가 자동으로 로그인하는 코드임. 

driver.get('https://mail.google.com/mail/u/0/#inbox')
time.sleep(3)