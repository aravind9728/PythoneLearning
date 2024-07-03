from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

#TODO application command

# to launch the website
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
# to get the page title
print(driver.title)
# to get the url for the page
print(driver.current_url)
# to get the page source
print(driver.page_source)

#TODO conditional command =====
# this commandans will return true or false

element = driver.find_elements(By.XPATH, "//*[@@name='login']")
print(element.is_displayed()) # this will return true when the element is present
print(element.is_enabled()) # this will return true when the element is active, if greyed out text box active for an condition
print(element.is_selected()) # for raido button and check box

#TODO broswer command

driver.close()
driver.quit()

#TODO Navigational command

driver.back() # navigate back to old page
driver.refresh() #refresh the page
driver.forward() # navigate to previous page




