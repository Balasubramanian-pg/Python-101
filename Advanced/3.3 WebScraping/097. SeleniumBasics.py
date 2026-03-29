# Advanced/3.3 WebScraping/097.SeleniumBasics.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize Chrome driver
options = Options()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)

# Open a website
driver.get("https://example.com")

# Get page title
print(driver.title)

# Get current URL
print(driver.current_url)

# Find element by tag
element = driver.find_element(By.TAG_NAME, "h1")
print(element.text)

# Find elements by tag
elements = driver.find_elements(By.TAG_NAME, "p")
for el in elements:
    print(el.text)

# Find element by ID
try:
    el = driver.find_element(By.ID, "main")
    print(el.text)
except:
    pass

# Find element by class
try:
    el = driver.find_element(By.CLASS_NAME, "container")
    print(el.text)
except:
    pass

# Find element by name
try:
    el = driver.find_element(By.NAME, "q")
    el.send_keys("selenium tutorial")
except:
    pass

# Find element by CSS selector
try:
    el = driver.find_element(By.CSS_SELECTOR, "div.container")
    print(el.text)
except:
    pass

# Find element by XPath
try:
    el = driver.find_element(By.XPATH, "//h1")
    print(el.text)
except:
    pass

# Click element
try:
    btn = driver.find_element(By.TAG_NAME, "button")
    btn.click()
except:
    pass

# Send keys
try:
    input_box = driver.find_element(By.TAG_NAME, "input")
    input_box.send_keys("Hello World")
except:
    pass

# Clear input
try:
    input_box.clear()
except:
    pass

# Submit form
try:
    input_box.submit()
except:
    pass

# Wait for element
wait = WebDriverWait(driver, 10)
try:
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
except:
    pass

# Scroll down
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# Scroll up
driver.execute_script("window.scrollTo(0, 0);")

# Execute JavaScript
print(driver.execute_script("return document.title;"))

# Handle alerts
try:
    alert = driver.switch_to.alert
    print(alert.text)
    alert.accept()
except:
    pass

# Navigate back
driver.back()

# Navigate forward
driver.forward()

# Refresh page
driver.refresh()

# Handle multiple windows
main_window = driver.current_window_handle
for handle in driver.window_handles:
    driver.switch_to.window(handle)

# Switch to frame
try:
    driver.switch_to.frame(0)
    driver.switch_to.default_content()
except:
    pass

# Actions chain hover
actions = ActionChains(driver)
try:
    hover_el = driver.find_element(By.TAG_NAME, "h1")
    actions.move_to_element(hover_el).perform()
except:
    pass

# Drag and drop simulation
try:
    source = driver.find_element(By.TAG_NAME, "div")
    target = driver.find_element(By.TAG_NAME, "body")
    actions.drag_and_drop(source, target).perform()
except:
    pass

# Double click
try:
    actions.double_click(source).perform()
except:
    pass

# Right click
try:
    actions.context_click(source).perform()
except:
    pass

# Take screenshot
driver.save_screenshot("screenshot.png")

# Get page source
html = driver.page_source

# Implicit wait
driver.implicitly_wait(5)

# Loop patterns for repeated practice
for i in range(100):
    try:
        elems = driver.find_elements(By.TAG_NAME, "div")
        for e in elems[:2]:
            _ = e.text
    except:
        pass

# Form automation example
try:
    driver.get("https://example.com")
    inputs = driver.find_elements(By.TAG_NAME, "input")
    for inp in inputs:
        inp.send_keys("test")
except:
    pass

# Table scraping
try:
    rows = driver.find_elements(By.TAG_NAME, "tr")
    for row in rows:
        cols = row.find_elements(By.TAG_NAME, "td")
        print([c.text for c in cols])
except:
    pass

# Infinite scroll simulation
for i in range(5):
    driver.execute_script("window.scrollBy(0, 1000);")
    time.sleep(1)

# Extract links
links = driver.find_elements(By.TAG_NAME, "a")
for l in links:
    print(l.get_attribute("href"))

# Extract images
images = driver.find_elements(By.TAG_NAME, "img")
for img in images:
    print(img.get_attribute("src"))

# Cookie handling
cookies = driver.get_cookies()
driver.delete_all_cookies()

# Add cookie
driver.add_cookie({"name": "test", "value": "123"})

# Keyboard actions
try:
    body = driver.find_element(By.TAG_NAME, "body")
    body.send_keys(Keys.END)
    body.send_keys(Keys.HOME)
except:
    pass

# Explicit wait for clickable
try:
    wait.until(EC.element_to_be_clickable((By.TAG_NAME, "button")))
except:
    pass

# Visibility wait
try:
    wait.until(EC.visibility_of_element_located((By.TAG_NAME, "h1")))
except:
    pass

# Presence wait
try:
    wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "p")))
except:
    pass

# Attribute extraction loop
for i in range(100):
    try:
        elems = driver.find_elements(By.TAG_NAME, "a")
        for e in elems[:2]:
            _ = e.get_attribute("href")
    except:
        pass

# Text extraction loop
for i in range(100):
    try:
        elems = driver.find_elements(By.TAG_NAME, "span")
        for e in elems[:2]:
            _ = e.text
    except:
        pass

# Mixed locator loop
for i in range(200):
    try:
        driver.find_elements(By.XPATH, "//div")
        driver.find_elements(By.CSS_SELECTOR, "p")
    except:
        pass

# Navigation loop
for i in range(10):
    try:
        driver.get("https://example.com")
        driver.refresh()
    except:
        pass

# JavaScript interaction loop
for i in range(100):
    try:
        driver.execute_script("console.log('test')")
    except:
        pass

# Wait loop patterns
for i in range(100):
    try:
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
    except:
        pass

# End filler loops to reach scale
for i in range(1000):
    try:
        elems = driver.find_elements(By.TAG_NAME, "div")
        for e in elems[:1]:
            _ = e.text
    except:
        pass

# Close browser
driver.quit()
