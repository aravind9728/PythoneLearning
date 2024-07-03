import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()
time.sleep(10)

# WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "//button[normalize-space()='Click for JS Prompt']"))).click()

driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Prompt']").click()

alert_win = driver.switch_to.alert

if alert_win.text == "I am a JS prompt":
    print("true")
else:
    print("False")

alert_win.send_keys("Aravind")
alert_win.accept()
text = "Aravind"

match_text = driver.find_elements(By.XPATH,"")
i=match_text.get_attribute("id")

string = match_text
list = string.split()
print(list)

