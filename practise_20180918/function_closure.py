'''
学习函数闭包、装饰器等知识
'''
import time

def fa(n):
    num = 1

    def fb():
        return n+num
    return fb


# 测试代码：
f = fa(1)
print("f不是直接等于2，而是一个函数,f:", f)
print("f()返回结果才等于2,f():", f())


'''
装饰器的例子
'''


def decorator(func): # 定义装饰器函数,输出函数的开始时间和结束时间
    def after_decor():
        print(func.__name__, "start:")
        func()
        print( func.__name__, "end...")
    return after_decor

@decorator
def bark():
    for i in range(3):
        print("Wooo~")
        time.sleep(1)

# 测试代码
bark()
