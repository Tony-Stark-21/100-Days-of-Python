import time

from bs4 import BeautifulSoup
from selenium import webdriver
import requests
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
dr_url = "https://docs.google.com/forms/d/e/1FAIpQLScS-eewzgjzcfTzvoan_a-xkTJTDlH93iU6dM042FX-iDj2_g/viewform?usp=dialog"


url = "https://appbrewery.github.io/Zillow-Clone/"
listings = []
Prices = []
Address = []
response = requests.get(url)
response.raise_for_status()
driver.get(dr_url)



soup = BeautifulSoup(response.content, "html.parser")
links = soup.select(selector=".result-list-container .List-c11n-8-84-3-photo-cards .StyledPropertyCardPhotoBody a[href]")

for li in links:
    listings.append(li.get("href"))
print(listings)


price = soup.select(selector=".result-list-container .List-c11n-8-84-3-photo-cards .StyledPropertyCardDataArea-fDSTNn span")
for amount in price:
    Prices.append(amount.text.strip().replace('/', ' ').split()[0].strip("+"))
print(Prices)

location = soup.select(selector=".result-list-container .List-c11n-8-84-3-photo-cards .StyledPropertyCardDataWrapper address")

for address in location:
    Address.append(address.text.strip("|").strip())
print(Address)

for address_item, price_item, link_item in zip(Address, Prices, listings):
    address_input = driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    time.sleep(1)
    address_input.send_keys(address_item)
    time.sleep(1)
    price_input = driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    time.sleep(1)
    price_input.send_keys(price_item)
    time.sleep(1)
    link_input = driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_input.send_keys(link_item)
    time.sleep(1)
    submit = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
    submit.click()
    time.sleep(2)
    another_response = driver.find_element(By.LINK_TEXT, "Submit another response")
    another_response.click()
    time.sleep(2)




