from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

#Instantiate the driver as a variable called browser
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

#Use browsers instance
browser.get("https://milani.rhi-staging.co.za/student-registration/")
browser.maximize_window()
#browser.quit()

#Locate the fields within the form
full_name = browser.find_element(By.ID, "input_9_21")
full_name.send_keys("PythonTester")

email = browser.find_element(By.ID, "input_9_12")
email.send_keys("pythontriggertest@rhidigital.co.za")

password = browser.find_element(By.ID, "input_9_20")
confirm_password = browser.find_element(By.ID, "input_9_20_2")
password.send_keys("J!ppoPy123@$")
confirm_password.send_keys("J!ppoPy123@$")

sponsor = browser.find_element(By.XPATH, value="//option[@value='Bidvest']")
sponsor.click()

register_button = browser.find_element(By.ID, "gform_submit_button_9")
register_button.click()

#Look for the next step after registration
assert browser.title == "Student Registration - Milani Education" 