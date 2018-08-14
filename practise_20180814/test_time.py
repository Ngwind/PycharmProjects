import time

'''
练习time模块的函数
主要函数有：
- time()
- localtime(secs)
- asctime(t)
- ctime(secs)
- strftime(format,t)
- strptime(str,format)
- mktime(t)
- gmtime(secs)
- clock()
- sleep(secs)
'''
t1 = time.time()  # time函数返回当前时间戳-float型数据
print("time函数返回当前时间戳-float型数据")
print(t1)
print(type(t1), "\n")

t2 = time.localtime(1493890956)  # localtime函数接受一个时间戳，返回一个时间元组
print("localtime函数接受一个时间戳，返回一个时间元组")
print(t2)
print(type(t2), "\n")

t3 = time.asctime(t2)  # asctime函数接受一个时间元组，返回一个格式化的字符串
print("asctime函数接受一个时间元组，返回一个格式化的字符串")
print(t3)
print(type(t3), "\n")

t4 = time.ctime(t1)  # ctime函数相当于localtime+asctime的结合
print("ctime函数相当于localtime+asctime的结合")
print(t4)
print(type(t4), "\n")

t5_1 = time.strftime('%Y-%m-%d %H:%M:%S %a %b', t2)  # strftime函数将时间元组转换成格式化时间字符串
t5_2 = time.strftime('%A %B %p %I:%M:%S %z')
print("strftime函数将时间元组转换成格式化时间字符串")
print(t5_1)
print(t5_2, '\n')

t6 = time.strptime('2018年8月14日10点3分45秒', '%Y年%m月%d日%H点%M分%S秒')  # strptime函数将字符串解析，输出时间元组
print("strptime函数将字符串解析，输出时间元组")
print(t6)
print(type(t6), "\n")

t7 = time.gmtime(t1)  # mgtime函数接收时间戳输出格林尼治时间元组
print("mgtime函数接收时间戳输出格林尼治时间元组，注意loacltime()是输出本地区的时间元组")
print(t7)
print(type(t7), "\n")

t8 = time.mktime(t7)  # mktime函数与gmtime函数相反，接收一个时间元组输出时间戳
print("mktime函数与gmtime函数相反，接收一个时间元组输出时间戳")
print(t8)
print(type(t8), "\n")

t9 = time.sleep(5)  # 推迟调用线程的运行，secs指秒数。
print("推迟调用线程的运行，secs指秒数。")
print(t9)
print(type(t9), "\n")

t10 = time.clock()  # 返回进程开始后的cpu运行时间
print("返回进程开始后的cpu运行时间")
print(t10)
print(type(t10), "\n")
