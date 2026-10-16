from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
# driver.get("https://www.amazon.com/dp/B0HGR4SDYC/ref=sspa_dk_detail_5?pd_rd_i=B0HGR4SDYC&pd_rd_w=pBUr1&content-id=amzn1.sym.4f5afe61-a551-4f21-a495-c7c4f2997a96&pf_rd_p=4f5afe61-a551-4f21-a495-c7c4f2997a96&pf_rd_r=N7M10YW67HZ89W49K6AA&pd_rd_wg=SvG1v&pd_rd_r=70184d89-09b4-4acf-9936-32276d56306c&sp_csd=d2lkZ2V0TmFtZT1zcF9kZXRhaWxfdGhlbWF0aWM&th=1")
#
# price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
# print(f"The price is {price_dollar.text}.{price_cents.text}")
driver.get("https://www.python.org/")
# search_bar = driver.find_element(By.NAME, value="q")
# print(search_bar.get_attribute("placeholder"))
# docs = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
# print(docs.text)
# link = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(link.text)
unordered = (driver.find_element(By.XPATH, value='//*[@id="content"]/div/section/div[2]/div[2]/div/ul'))
event_times = driver.find_elements(By.CSS_SELECTOR, value='.event-widget time')
for time in event_times:
    print(time.text)
event_names = driver.find_elements(By.CSS_SELECTOR, value='.event-widget li a')
for name in event_names:
    print(name.text)
events = {}

for n in range(len(event_times)):
    events[n] = {
        "time":event_times[n].text,
        "name":event_names[n].text
    }

print(events)
driver.quit()