import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
mywait = WebDriverWait(driver,10,poll_frequency=2, ignored_exceptions=Exception)
driver.get("url")
driver.maximize_window()
# this will wait for the locators whereever the driver mentioned
driver.implicitly_wait(10)

driver.find_elements(By.NAME,"")

# this will for the mentioned time
time.sleep(10)

# this will for explicitly for the locator
mywait.until(EC.presence_of_all_elements_located("xpath"))  #mywait -object, until -condition
mywait.until(EC.visibility_of_element_located((By.TAG_NAME, 'br')))
