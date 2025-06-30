from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# ✅ Set options to keep Chrome open after script finishes
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)  # Keeps browser open

# ✅ Initialize WebDriver with the options
driver = webdriver.Chrome(options=options)

# ✅ Open Google
driver.get("https://www.google.com")

# ✅ Wait for page to load
time.sleep(2)

# ✅ Find the search input box by its name attribute
search_box = driver.find_element(By.NAME, "q")

# ✅ Type the search text into the box
search_box.send_keys("Search this string")

# ✅ Simulate pressing the Enter key
#search_box.send_keys(Keys.RETURN)

# ✅ Wait for results (optional)
time.sleep(5)

# ❌ No driver.quit() — browser stays open

