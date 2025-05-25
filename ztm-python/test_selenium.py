from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_browser = webdriver.Chrome()
chrome_browser.get('https://magento.softwaretestingboard.com/')
element = chrome_browser.find_element(By.CLASS_NAME, "action tocart primary")

print(element.text)  # Should show "Add to Cart"
print(element.get_attribute("title"))  # Should show "Add to Cart"