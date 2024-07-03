import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
mywait = WebDriverWait(driver,10,poll_frequency=2)

driver.maximize_window()
driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
# mywait.until(EC.presence_of_all_elements_located(By.XPATH,''))
mywait.until(EC.visibility_of_element_located((By.XPATH, "//p[contains(text(),'Congratulations')]")))
element = driver.find_element(By.XPATH,"//p[contains(text(),'Congratulations')]")
# print(element.text)


assert element.text == "Congratulations! You must have the proper credentials."
print("Logged in")



