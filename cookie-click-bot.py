'''
This project is automated click bot for Cookie Clicker game (https://orteil.dashnet.org/cookieclicker/).
Have fun with it!
'''


from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://orteil.dashnet.org/cookieclicker/')

time.sleep(3)
lang_select = driver.find_element(By.ID, value='langSelect-EN')
lang_select.click()

cookie = driver.find_element(By.ID, value='bigCookie')
while True:
    timeout = time.time() + 10
    while time.time() < timeout:
        cookie.click()

    add_ons_list = driver.find_elements(By.CSS_SELECTOR, value="#products .unlocked.enabled")
    add_ons_list[-1].click()