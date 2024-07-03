import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.techlistic.com/p/selenium-practice-form.html")


#TODO multiple element find elements
checkboxs = driver.find_elements(By.XPATH,"//input[@type='checkbox']")

# for check in checkbox:
#     check.click()

for checkbox in checkboxs:
    weekname = checkbox.get_attribute("id")
    if weekname == "tool-2" and weekname == "profession-0":
        checkbox.click()


for i in range(len(checkboxs))-2, len(checkboxs):
    checkboxs[i].click()




time.sleep(5)


