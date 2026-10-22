import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import load_dotenv as dotenv
dotenv.load_dotenv()
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


SIMILAR_ACCOUNT = "chefsteps"
USERNAME = os.environ.get("USERNAMES")
PASSWORD = os.getenv("PASSWORD")
BASE_URL = "https://app.100daysofpython.dev/services/share-a-naan"

class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get(BASE_URL)
    def login(self):
        email = self.driver.find_element(By.XPATH, "/html/body/div/aside/div/form/input[1]")
        time.sleep(1)
        email.send_keys(USERNAME)
        password = self.driver.find_element(By.XPATH,"/html/body/div/aside/div/form/input[2]")
        time.sleep(1)
        password.send_keys(PASSWORD)
        time.sleep(1)
        submit = self.driver.find_element(By.CLASS_NAME, "naan-welcome-submit")
        submit.click()
        time.sleep(2)
        popup = self.driver.find_element(By.CLASS_NAME,"naan-popup-dismiss")
        time.sleep(1)
        popup.click()
        time.sleep(5)
        wait2 = self.driver.find_element(By.CSS_SELECTOR,".naan-popup-card button.naan-popup-dismiss")
        time.sleep(1)
        wait2.click()
    def find_followers(self):
        search = self.driver.find_element(By.CSS_SELECTOR,".naan-rail button.naan-rail-item")
        search.click()
        time.sleep(2)
        search_results = self.driver.find_element(By.CLASS_NAME,"naan-search-row")
        search_results.click()
        followers = self.driver.find_element(By.CLASS_NAME,"naan-followers-link")
        followers.click()
        scroll = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME,"followers-scroll")))
        for _ in range(5):
            self.driver.execute_script(
                "arguments[0].scrollTop = arguments[0].scrollHeight",
                scroll
            )
            time.sleep(1)
    def follow(self):
        scroll = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME,"followers-scroll")))
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "naan-follow-btn")))

        buttons = scroll.find_elements(By.CLASS_NAME, "naan-follow-btn")

        for btn in buttons:
            try:
                self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", btn)
                time.sleep(0.5)
                btn.click()
                time.sleep(1)
            except Exception as e:
                print(f"Skipped a button due to: {e}")
                '''The follow part was aided by Gemini so i won't take credit for it'''
bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()