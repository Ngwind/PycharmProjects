from selenium import webdriver
from selenium.webdriver.common.keys import Keys
'''
这是一个selenium的小例子
- 打开python.org网站 ，断言页面标题是否为Python
- 在search框输入pycon，断言是否有搜索结果
- 最后关闭浏览器
'''

driver = webdriver.Chrome()
driver.get("http://www.python.org")
assert "Python" in driver.title

elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No result found." not in driver.page_source
driver.close()



