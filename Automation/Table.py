import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:\\Users\\aravi\\AppData\\Local\\Programs\\Python\\Python312\\Scripts\\chromedriver.exe")
driver=webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(3)

# rows = driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr")
# count = 0
# for data in rows:
#     count+=1
#     print(count)
#TODO print no of rows and column
noofrows = len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr"))
noofcol = len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//th"))
print(noofrows)
print(noofcol)

#TODO print specific row and column value
rowvalue = driver.find_element(By.XPATH,"//table[@name='BookTable']//tr[5]//td[1]")
print(rowvalue.text)

#TODO print all the rows and column
for r in range(2,noofrows+1):
    for c in range(1,noofcol+1):
        data = driver.find_element(By.XPATH,"//table[@name='BookTable']//tr["+str(r)+"]//td["+str(c)+"]")
        print(data.text,end=" ")
    print()



for r in range(2,noofrows+1):
    authorName = driver.find_element(By.XPATH,"//table[@name='BookTable']//tr["+str(r)+"]//td[2]").text
    if authorName == "Mukesh":
        bookname = driver.find_element(By.XPATH,"//table[@name='BookTable']//tr["+str(r)+"]//td[1]").text
        print(authorName,"--",bookname)
