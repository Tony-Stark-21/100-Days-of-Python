import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
chrome_options = uc.ChromeOptions()
# chrome_options.add_experimental_option("detach", True)
driver = uc.Chrome(options=chrome_options)

# driver.get("https://en.wikipedia.org/wiki/Main_Page")
# need = driver.find_element(By.CSS_SELECTOR, value="#articlecount li a span")
# need.click()
#
# all_portals = driver.find_element(By.LINK_TEXT, value="Help desk")
# all_portals.click()
#
#
# search = driver.find_element(By.NAME, value="search")
# driver.get("https://appbrewery.github.io/fake-newsletter-signup/")
# fname = driver.find_element(By.NAME, value="fName")
# fname.send_keys("Arthur")
#
# lname = driver.find_element(By.NAME, value="lName")
# lname.send_keys("Reynolds")
#
# email = driver.find_element(By.NAME, value="email")
# email.send_keys("arthurreynolds2121@gmail.com")
#
# submit = driver.find_element(By.CSS_SELECTOR, value=".text-center button")
# submit.click()
# driver.quit()

driver.get("https://orteil.dashnet.org/cookieclicker/")
time.sleep(3)
lang = driver.find_element(By.ID, value="langSelect-EN")
lang.click()
time.sleep(3)
got_it = driver.find_element(By.CSS_SELECTOR, value=".cc_container--open a")
got_it.click()
time.sleep(3)
eng_button = driver.find_element(By.ID, value="bigCookie")
start_time = time.time()
while True:
    try:
        cookies = driver.find_element(By.ID, value="cookies")
        eng_button.click()
        time.sleep(0.01)
        if time.time() - start_time >= 5:
            if float(cookies.text.split()[0].replace(",","")) >= 100:
                check_second = driver.find_element(By.ID, value="product1")
                check_second.click()
            elif float(cookies.text.split()[0].replace(",","")) >= 15:
                check_first = driver.find_element(By.ID, value="product0")
                check_first.click()
            start_time = time.time()
    except Exception as e:
        print("Clicking stopped", e)
        break