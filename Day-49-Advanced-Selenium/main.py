from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import os
import time
ACCOUNT_EMAIL = "student@test.com"
ACCOUNT_PASSWORD = "password123"
GYM_URL = "https://appbrewery.github.io/gym/"

prefs = {
    "profile.password_manager_leak_detection": False,
    "credentials_enable_service": False,
}

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_experimental_option("prefs", prefs)
user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
driver = webdriver.Chrome(options=chrome_options)
driver.get(GYM_URL)

wait = WebDriverWait(driver, 2)

# driver.implicitly_wait(10)
login = driver.find_element(By.ID, "login-button")
login.click()

email_input = wait.until(ec.presence_of_element_located((By.ID, "email-input")))
email_input.send_keys(ACCOUNT_EMAIL)

password_field = driver.find_element(By.ID, "password-input")
password_field.send_keys(ACCOUNT_PASSWORD)

login_button = driver.find_element(By.ID, "submit-button")
login_button.click()

wait.until(ec.presence_of_element_located((By.ID, "schedule-page")))
# tuesday_booking = driver.find_element(By.ID, "book-button-spin-2026-10-20-1800")
# tuesday_booking.click()
# print("Booked🦋. Spin class on Tuesday,October 20💫🕺")
# driver.quit()

class_cards = driver.find_elements(By.CSS_SELECTOR, "div[id^='class-card-']")
already_booked_count = 0
booked_count = 0
waitlist_count = 0
processed_classes = []

for cards in class_cards:
    day_group = cards.find_element(By.XPATH, "./ancestor::div[contains(@id, 'day-group-')]")
    '''from my understanding, it checks inside the ancestor which is inside all the div with id class_card,
    slices through two divs then lands to find id which is why we use@id but now we specified the id
     which is day-group-'''
    day_title = day_group.find_element(By.TAG_NAME, "h2").text
    '''Now what this does is that it checks inside day_group for a tag name of h2 which bears the day of the course. '''

        # Check if this is a Tuesday OR Thursday
    if "Tue" in day_title or "Thu" in day_title:
        time_text = cards.find_element(By.CSS_SELECTOR, "p[id^='class-time-']").text
        if "6:00 PM" in time_text:
                class_name = cards.find_element(By.CSS_SELECTOR, "h3[id^='class-name-']").text
                button = cards.find_element(By.CSS_SELECTOR, "button[id^='book-button-']")

                # Track the class details
                class_info = f"{class_name} on {day_title}"

                if button.text == "Booked":
                    print(f"✓ Already booked: {class_info}")
                    already_booked_count += 1
                    # Add detailed class info
                    processed_classes.append(f"[Booked] {class_info}")
                elif button.text == "Waitlisted":
                    print(f"✓ Already on waitlist: {class_info}")
                    already_booked_count += 1
                    # Add detailed class info
                    processed_classes.append(f"[Waitlisted] {class_info}")
                elif button.text == "Book Class":
                    button.click()
                    print(f"✓ Successfully booked: {class_info}")
                    booked_count += 1
                    # Add detailed class info
                    processed_classes.append(f"[New Booking] {class_info}")
                    time.sleep(0.5)
                elif button.text == "Join Waitlist":
                    button.click()
                    print(f"✓ Joined waitlist for: {class_info}")
                    waitlist_count += 1
                    # Add detailed class info
                    processed_classes.append(f"[New Waitlist] {class_info}")
                    time.sleep(0.5)

print("\n--- BOOKING SUMMARY ---")
print(f"New bookings: {booked_count}")
print(f"New waitlist entries: {waitlist_count}")
print(f"Already booked/waitlisted: {already_booked_count}")
print(f"Total Tuesday & Thursday 6pm classes: {booked_count + waitlist_count + already_booked_count}")

    # Print detailed class list
print("\n--- DETAILED CLASS LIST ---")
for class_detail in processed_classes:
        print(f"  • {class_detail}")


        '''Now this remaining parts mean that if there is tue in the day title, it should look 
            for time by checking for the id of class-time-, then it checks for the name of the 
            class by class-name- then once all these conditions are met, it looks for the 
            button under the conditions and click on it.
            OMO most of this stuff i didn't do it myself'''
check = driver.find_element(By.ID, "my-bookings-link")
check.click()
print(check.text)
'''I checked myself and couldn't get the number of bookings made
Gemini aided me in brainstorming it. '''
time.sleep(2)
booked_elements = driver.find_elements(By.CSS_SELECTOR, "div[id^='booking-card-booking_")
number_of_bookings = len(booked_elements)
print(f"Total number of bookings: {number_of_bookings}")
'''booking2 = driver.find_element(By.ID, "my-bookings-page")
bb = booking2.get_attribute("data-bookings-count")
ba = int(bb)
print(ba)'''
