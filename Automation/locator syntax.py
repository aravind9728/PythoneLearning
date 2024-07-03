from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.find_elements(By.NAME, "name")
driver.find_elements(By.XPATH, "xpath")
driver.find_elements(By.LINK_TEXT, "link text")
driver.find_elements(By.PARTIAL_LINK_TEXT, "partial link text")
driver.find_elements(By.TAG_NAME, "tag name")
driver.find_elements(By.CLASS_NAME, "class name")
driver.find_elements(By.CSS_SELECTOR, "css selector")

#linktext

#partial linktext
driver.find_element(By.LINK_TEXT,'Images')
driver.find_elements(By.PARTIAL_LINK_TEXT,'Ima')

# CSS selectors
driver.find_elements(By.CSS_SELECTOR, "div#emailError") # by ID - tagename#id
driver.find_elements(By.CSS_SELECTOR, "#emailError") #by ID - #id without tage name

driver.find_elements(By.CSS_SELECTOR, "input.inputtext")  #byclass  tagename.classvaule
driver.find_elements(By.CSS_SELECTOR, ".inputtext _55r1 _6luy")  #byclass .classvaule without class name

driver.find_elements(By.CSS_SELECTOR, "input[name=email]")  #by attribute tagename[attribute = value] other than ID and class we can use this
driver.find_elements(By.CSS_SELECTOR, "[name=email]")  #by attribute [attribute = value] without tage name

#when there is duplicate class name
driver.find_elements(By.CSS_SELECTOR, "input.inputtext[name=pass]")  #by class attribute tagename.classvalue[attribute = value]
driver.find_elements(By.CSS_SELECTOR, ".inputtext[name=pass]")  #by class attribute tagename.classvalue[attribute = value]  without tage name

# '*' will search whole html
driver.find_elements(By.XPATH, "//*[@@name='login']")

#TODO get_attribute
element = driver.find_elements(By.XPATH, "//*[@@name='login']")
element.get_attribute()

#and
driver.find_elements(By.XPATH, "//button[@class='_42ft' and @name='login']")
#or
driver.find_elements(By.XPATH, "//button[@class='_42ft' or @name='login']")

#tagename[contains(@attribute,value)] attribute value can be partial
driver.find_elements(By.XPATH, "//input[contains(@value,Feeling)]")

#starts-with
driver.find_elements(By.XPATH, "//input[starts-with(@value,gN)]")

#text()
driver.find_elements(By.XPATH, "//a[text()='Gmail']")

#self
driver.find_elements(By.XPATH, "//input[contains(@name,password)]/self::input")

#parent
driver.find_elements(By.XPATH, "//input[contains(@name,password)]/parent::form']")



