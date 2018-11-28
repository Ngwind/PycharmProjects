from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("http://localhost:4000/")
sleep(5)
driver.quit()
