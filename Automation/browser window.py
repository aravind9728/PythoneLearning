import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/windows")
driver.maximize_window()

window =driver.current_window_handle #TODO - used to handle single window
print(window) # this will capture single window ID
time.sleep(4)
driver.find_element(By.LINK_TEXT,"Click Here").click()
time.sleep(10)
print(driver.title)
if driver.title == "The Internet":
    print("navigates successfully")
else:
    print("navigating error")

time.sleep(3)
Windowids =driver.window_handles

parent_window = Windowids[0]
child_window = Windowids[1]
print(child_window)

driver.switch_to.window(parent_window)
print(driver.title)
time.sleep(3)
driver.switch_to.window(child_window)
print(driver.title)
time.sleep(3)
driver.switch_to.window(child_window)
driver.close()
time.sleep(3)

# for windows in Windowids:
#     driver.switch_to.window(windows)
#     print(driver.title)

