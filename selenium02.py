from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

binary = FirefoxBinary('C:\\Program Files\\Mozilla Firefox\\firefox.exe')
caps = DesiredCapabilities().FIREFOX
caps["marionette"] = True
driver = webdriver.Firefox(capabilities=caps, firefox_binary=binary, executable_path="C:\\Utility\\BrowserDrivers\\geckodriver.exe")

driver.get("https://accounts.google.com/signin")
email_phone = driver.find_element_by_css_selector("#identifierId")
email_phone.send_keys("01039996540")
driver.find_element_by_css_selector(".ZFr60d.CeoRYc").click()
password = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "input[class='whsOnd zHQkBf'][type='password']"))
)
password.send_keys("#a1034817")
driver.find_element_by_css_selector(".ZFr60d.CeoRYc").click()