# from selenium import webdriver
#
#
# driver = webdriver.Chrome("C/Drivers/chromedriver.exe")


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

from selenium.webdriver.common.by import By

# chrome_service = Service("C:\Drivers\chromedriver.exe")
# driver = webdriver.Chrome(service=chrome_service)
driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
driver.implicitly_wait(20)

driver.find_element("xpath","//input[@name='username']").send_keys('Admin')
driver.find_element("xpath","//input[@name='password']").send_keys('admin123')

driver.find_element("xpath","//button[@type='submit']").click()

actual_title = driver.title
expected_title = "OrangeHRM"
if actual_title == expected_title:
    print("Test case passed")
else:
    print("Test case failed")

search = driver.find_element("xpath","//input[@name='password']").send_keys('admin123')
print(search.is_displayed())



