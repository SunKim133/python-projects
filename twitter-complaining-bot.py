from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
import time

PROMISED_DOWN = 75
PROMISED_UP = 15
X_ID = os.environ.get('X_ID')
X_PASSWORD = os.environ.get('X_PASSWORD')

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(options=chrome_options)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get('https://www.speedtest.net/')
        self.start = self.driver.find_element(By.CLASS_NAME, value='test-mode-multi')
        time.sleep(10)
        self.start.click()
        time.sleep(60)
        self.down = self.driver.find_element(By.CLASS_NAME, value='download-speed').text
        self.up = self.driver.find_element(By.CLASS_NAME, value='upload-speed').text
        print(f"down: {self.down}\nup: {self.up}")

    def tweet_at_provider(self):
        self.driver.get('https://twitter.com/login')
        time.sleep(5)
        id = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        id.send_keys(X_ID + Keys.ENTER)
        time.sleep(5)
        password = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        password.send_keys(X_PASSWORD + Keys.ENTER)
        time.sleep(10)
        tweet = f"Hey Telus, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
        posting = self.driver.find_element(By.CSS_SELECTOR, value='br[data-text="true"]')
        posting.send_keys(tweet)
        send_key = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[3]/div/span')
        send_key.click()

my_bot = InternetSpeedTwitterBot()
my_bot.get_internet_speed()
my_bot.tweet_at_provider()
