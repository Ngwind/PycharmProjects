from selenium import webdriverfrom time import sleep'''定位页面element的方法主要有几种：- 通过ID查找元素- 通过name查找元素- 通过Xpath查找元素- 通过链接文本查找元素- 通过标签名查找元素- 通过Class name查找元素- 通过CSS选择器查找元素  以"find_element_by"开头方法返回页面中第一个匹配的元素;以“find_elements_by”开头方法返回页面中所有匹配的元素;'''def waiting(elem, arg):  # +1s        elem.send_keys(arg)        sleep(1)driver = webdriver.Chrome()driver.get("file://C:/Users/Administrator/Desktop/learn-selenium.html")'''使用find_element_by_id()'''elem_form = driver.find_element_by_id("loginForm")'''使用find_element_by_name()'''elem_username = driver.find_element_by_name("username")elem_password = driver.find_element_by_name("password")elem_continue = driver.find_elements_by_name("continue")  # 这里使用elemnets返回所有匹配的元素elem_submit = elem_continue[0]elem_clear = elem_continue[1]waiting(elem_username, "wwdwwdwwd")waiting(elem_password, "123456")elem_submit.click()assert "username" in driver.current_url'''使用find_element_by_xpath()'''clear_button = driver.find_element_by_xpath("//input[@name='continue'][@type='button']")elem_p = driver.find_element_by_xpath("//p")'''使用find_elemnet_by_link'''continue_link = driver.find_element_by_link_text('Continue')continue_link = driver.find_element_by_partial_link_text('Conti')'''使用find_element_by_tag_name'''elem_form_tag = driver.find_element_by_tag_name("form")'''使用find_element_by_class_name'''elem_content = driver.find_element_by_class_name("content")'''使用find_element_by_css_selector'''elem_continue_css = driver.find_element_by_css_selector("p.content")driver.close()