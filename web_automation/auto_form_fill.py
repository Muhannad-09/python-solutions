from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Path to your chromedriver (change this if needed)
driver_path = "C:/WebDrivers/chromedriver.exe"

# Launch Chrome
driver = webdriver.Chrome(executable_path=driver_path)

# Open the website
driver.get("https://www.saucedemo.com")

# Wait for the page to load
time.sleep(2)

# Fill in username and password
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")

# Click the login button
driver.find_element(By.ID, "login-button").click()

# Wait and then close browser
time.sleep(5)
driver.quit()
