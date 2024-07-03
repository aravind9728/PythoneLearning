import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.opencart.com/index.php?route=account/register")
time.sleep(60)
drop = driver.find_element(By.XPATH,"//select[@name='country_id']")

seledrop = Select(drop)

seledrop.select_by_visible_text("American Samoa")
seledrop.select_by_value('12') #it's the value attribute should be given in quotes
seledrop.select_by_index(6) # its just the index of the element

#count the total no of dropdpwn value
alloptions = seledrop.options
print("total no options",len(alloptions))

#print the dropdown values
for opt in alloptions:
    print(opt.text)

# no bulit in function

for allopt in alloptions:
    if allopt.text == "india":
        allopt.click()
        break