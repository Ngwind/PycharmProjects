"""

"""

from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
elem = driver.find_element_by_name("wd")
#  attribute是html标签上的特性，它的值只能够是字符串；property是DOM中的属性，是javascript里的对象
print(type(elem.get_attribute("value")), type(elem.get_property("id")),elem.location)
sleep(1)
driver.quit()
