from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.expected_conditions import element_to_be_clickable
from selenium.webdriver.support.ui import WebDriverWait

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


TINDOG_URL = "https://app.100daysofpython.dev/services/tindog/u/0RXjzNS1MY03Brv5XzWddg9KSCovODLD"
'''Well, here we are . I kinda had issue with this for some reason'''
driver = webdriver.Chrome(options=chrome_options)
driver.get(TINDOG_URL)

wait = WebDriverWait(driver, 2)

login = driver.find_element(By.CLASS_NAME, "tindog-login-pill")
login.click()

time.sleep(2)
# wait.until(ec.presence_of_element_located((By.CLASS_NAME, "tindog-modal")))
base_window = driver.window_handles[0]

face_bark = driver.find_element(By.CLASS_NAME, "btn-facebark")
face_bark.click()

time.sleep(2)
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)

email = driver.find_element(By.ID, "email")
email.send_keys("arthurreynolds2121@gmail.com")
time.sleep(1)
password = driver.find_element(By.ID, "pass")
password.send_keys("Pythontest3")
time.sleep(1)
submit = driver.find_element(By.XPATH, "/html/body/div[2]/div/form/button")
submit.click()

driver.switch_to.window(base_window)
allow1 = driver.find_element(By.XPATH, "/html/body/main/div/div/form/button")
allow1.click()
time.sleep(2)
enable = driver.find_element(By.XPATH, "/html/body/main/div/div/form/button[1]")
enable.click()
accept = driver.find_element(By.XPATH, "/html/body/main/div/div/form/button")
accept.click()
like = driver.find_element(By.ID, "like-button-container")
while True:
    try:
        wait.until(element_to_be_clickable(like))
        like.click()
        time.sleep(4)
    except ElementClickInterceptedException:
        try:
            driver.find_element(By.CSS_SELECTOR, value='.match-popup a').click()
        except NoSuchElementException:
            time.sleep(2)


