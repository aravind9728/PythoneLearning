import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
time.sleep(5)

driver.find_element(By.XPATH,"//input[@class='wikipedia-search-input']").send_keys("Selenium")
driver.find_element(By.XPATH,"//input[@type='submit']").click()
time.sleep(5)
elements = driver.find_elements(By.XPATH,"//div[@id='wikipedia-search-result-link']//a")

for count in elements:
    print(count.text)

for link in elements:
    print(link.get_attribute('href'))
time.sleep(3)

Windowids =driver.window_handles
p = driver.current_window_handle

#get first child window

for w in Windowids:
#switch focus to child window
    if(w!=p):
        driver.switch_to.window(w)
    break


for link_click in elements:
    link_click.click()
    for windows in Windowids:
        driver.switch_to.window(windows)
        print(driver.title)


time.sleep(3)

driver.quit()