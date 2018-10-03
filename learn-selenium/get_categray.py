from selenium import webdriver


driver = webdriver.Chrome()
driver.get("file:///C:/Users/Administrator/Desktop/t.html")
a_list = driver.find_elements_by_xpath('//span[@class="articlename"]')
session_list = []
for i in a_list:
    session_list.append(i.text)
print(session_list)