from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://www.python.org")

print(driver.title)
print(driver.current_url)
print(driver.page_source)
print(driver.find_element_by_name("q"))