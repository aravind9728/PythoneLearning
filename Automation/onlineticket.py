import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

ser_obj = Service("C:\\Drivers\\chromedriver.exe")
driver = webdriver.Chrome(service=ser_obj)
driver.get("https://www.dummyticket.com/")
driver.maximize_window()
driver.implicitly_wait(5)

driver.find_element(By.XPATH,"//a[text()='Buy Ticket']").click()
driver.find_element(By.XPATH,"//input[@id='product_551']").click()
driver.find_element(By.XPATH,"//input[@id='dob']").click()

driver.find_element(By.XPATH,"//input[@id='travname']").send_keys("TesterFirstname")
driver.find_element(By.XPATH,"//input[@id='travlastname']").send_keys("lastname")
select_mon = Select(driver.find_element(By.XPATH,"//select[@data-handler='selectMonth']"))
select_mon.select_by_visible_text("Jan")
time.sleep(5)
select_year = Select(driver.find_element(By.XPATH,"//select[@data-handler='selectYear']"))
select_year.select_by_visible_text("1997")
all_dates = driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']//a")

for dates in all_dates:
    if dates.text == "28":
        dates.click()
        break

driver.find_element(By.XPATH,"//input[@id='sex_1']").click()
driver.find_element(By.XPATH,"//input[@id='traveltype_2']").click()
driver.find_element(By.XPATH,"//input[@id='fromcity']").send_keys("Chennai")
driver.find_element(By.XPATH,"//input[@id='tocity']").send_keys("japan")
driver.find_element(By.XPATH,"//input[@id='billing_phone']").send_keys("1234567890")
driver.find_element(By.XPATH,"//input[@id='billing_email']").send_keys("tesr@test.com")

select_country = Select(driver.find_element(By.XPATH,"//span[@id='select2-billing_country-container']"))
select_country.select_by_visible_text("Japan")
