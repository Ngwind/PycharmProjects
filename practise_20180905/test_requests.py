import requests
import json
'''
1.get请求
2.post请求
3.响应状态码
4.响应正文文本
5.响应头部
6.cookies
'''

'''
https://postman-echo.com/get
'''

p = {'number': 123, 'name': 'wwd'}  # url参数
r = requests.get('https://postman-echo.com/get', params=p)  # 用get函数发起get请求，url参数传给params
print(type(r))  # 返回response对象


