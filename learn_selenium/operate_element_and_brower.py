"""
练习对元素和浏览器的基本操作
元素：

浏览器：

"""
from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()
driver.get("http://baidu.com")
elem_input = driver.find_element_by_name("wd")
elem_input.clear()
sleep(1)
elem_input.send_keys("深信服测试工程师笔试")
sleep(3)
elem_input.submit()
sleep(3)

driver.refresh()  # 刷新
sleep(1)
driver.back() # 后退
sleep(1)
driver.forward()  # 前进
sleep(1)
driver.minimize_window()  # 最小化
sleep(1)
driver.set_window_rect(100,200,500,600)   # 设置位置大小
sleep(1)
driver.maximize_window()  # 最大化
sleep(1)
print(driver.get_log("browser"))
sleep(1)
driver.quit()  #　关闭浏览器