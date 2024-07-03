from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:\\Users\\aravi\\AppData\\Local\\Programs\\Python\\Python312\\Scripts\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")


driver.find_element(By.XPATH,"//input[@name='username']").send_keys("Admin")
driver.find_element(By.XPATH,"//input[@name='password']").send_keys("admin123")
driver.find_element(By.XPATH,"//button[@type='submit']").click()

driver.find_element(By.XPATH,"//span[text()='Admin']").click()

row_len = len(driver.find_elements(By.XPATH,""))
print(row_len)

count = 0
for r in range(1,row_len+1):
    status = driver.find_element(By.XPATH,"").text
    if status == "Enabled":
        count=+1

print("total no of users",row_len)
print("total no of enabled",count)
print("total no of disabled",(row_len-count))