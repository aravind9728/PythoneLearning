import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:\\Users\\aravi\\AppData\\Local\\Programs\\Python\\Python312\\Scripts\\chromedriver.exe")
driver=webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(3)



Act = ActionChains()

test = driver.find_element()
source = driver.find_element()
target = driver.find_element()

Act.move_to_element(test).perform()  #TODO mouse hover
Act.context_click(test).perform()  #TODO righclick
Act.double_click(test).perform()  #TODO  double click
Act.drag_and_drop(source,target)  #TODO  drage and drop
Act.drag_and_drop_by_offset(test,39,0)  #TODO slider


#TODO Scrolling
driver.execute_script("window.scrollBy(0,3000)","") #TODO by value
driver.execute_script("argument[0].scrollIntoView();",test) #TODO by locator
driver.execute_script("window.scrollBy(0,document.body.scrollHeight") # t++TODO the end

Act.key_down(Keys.CONTROL).send_keys("A").key_up(Keys.CONTROL).perform() #TODO select all
Act.key_down(Keys.CONTROL).send_keys("C").key_up(Keys.CONTROL).perform() # TODO Copy
Act.key_down(Keys.CONTROL).send_keys("V").key_up(Keys.CONTROL).perform() #TODO Past
Act.send_keys(Keys.TAB).perform() #TODO to use tab

#TODO screenshot
driver.save_screenshot("path")

#TODO open link in new tab ctrl +enter
driver.find_element("").send_keys(Keys.CONTROL+Keys.RETURN) # open the link in new tab

driver.get("1url")
driver.switch_to.new_window("tab") #this will open new tab
driver.switch_to.new_window("window") #this will open new brower window
driver.get("url2")

