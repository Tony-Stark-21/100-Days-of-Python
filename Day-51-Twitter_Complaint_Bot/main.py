import time
import os
import undetected_chromedriver as uc
import load_dotenv
from selenium.webdriver.support import expected_conditions as ec
# from selenium import webdriver
'''Well, I didn't use webdriver coz of some connection error'''
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

chrome_options = uc.ChromeOptions()
load_dotenv.load_dotenv()

PROMISED_DOWN = 50
PROMISED_UP = 15
Y_EMAIL = os.environ.get("Y_EMAIL")
Y_PASSWORD = os.environ.get("Y_PASSWORD")
Y_LOGIN_URL = "https://app.100daysofpython.dev/services/y/login"


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = uc.Chrome(options=chrome_options,version_main=155)
        self.down = PROMISED_DOWN
        self.up = PROMISED_UP
        self.download = 0.0
        self.upload = 0.0
    def get_internet_speed(self):
        try:
            self.driver.get(url="https://speedtest.net")
            time.sleep(3)
            snub = self.driver.find_element(By.ID, "onetrust-button-group")
            snub.click()
            time.sleep(2)
            go = self.driver.find_element(By.CSS_SELECTOR, "div button h1")
            go.click()
            test_wait = WebDriverWait(self.driver, 120)
            download_rate = test_wait.until(ec.visibility_of_element_located((By.XPATH, '(//h3[@class="font-mono py-2 text-5xl MuiBox-root css-s31qlv"])[1]')))
            self.download = float(download_rate.text.split()[0].strip().replace(",",""))

            upload_rate = test_wait.until(ec.visibility_of_element_located((By.XPATH, '(//h3[@class="font-mono py-2 text-5xl MuiBox-root css-s31qlv"])[2]')))
            self.upload = float(upload_rate.text.split()[0].strip().replace(",",""))
            print(f"Download:{self.download}, Upload:{self.upload}")
        except Exception as e:
            print(e)


    def tweet_at_provider(self):
        self.driver.get(Y_LOGIN_URL)
        time.sleep(2)
        email = self.driver.find_element(By.ID, "email")
        email.send_keys(Y_EMAIL)
        time.sleep(2)
        password = self.driver.find_element(By.ID, "password")
        password.send_keys(Y_PASSWORD)
        time.sleep(2)
        submit = self.driver.find_element(By.CLASS_NAME, "y-login-submit")
        submit.click()
        time.sleep(5)
        post_button = self.driver.find_element(By.CLASS_NAME, "x-post-cta")
        post_button.click()
        text_space = self.driver.find_element(By.ID,"modal-compose")
        text_space.send_keys(f'Disappointed with my connection today @MTNNG. Speedtest shows {self.download} Mbps down / {self.upload} Mbps up. My plan promised {PROMISED_DOWN} Mbps down. What is going on?')
        post = self.driver.find_element(By.ID, "modal-post-btn")
        post.click()

bot = InternetSpeedTwitterBot()
bot.get_internet_speed()

if bot.download < bot.down:
    bot.tweet_at_provider()

input("Press Enter to completely close the browser and exit...")
bot.driver.quit()
