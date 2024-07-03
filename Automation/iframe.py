from selenium import webdriver

driver =webdriver.Chrome()
driver.get("")
driver.maximize_window()

driver.switch_to.frame("") # this will switch from the main to child frame
#TODO -- switch_to.frame("name of the frame"), switch_to.frame("id of the frame"), switch_to.frame("web element"),switch_to.frame("0")
driver.find_element("")
driver.switch_to.default_content()

driver.switch_to.frame("")
driver.find_element("")