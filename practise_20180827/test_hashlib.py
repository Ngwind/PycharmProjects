import hashlib
'''
hashlib模块用来进行hash函数处理.一般通过"haslib.hash函数名()"来获得一个hash函数对象。
hash函数对象有下列方法：
 - update(arg) ：使用arg中的字节更新哈希对象。 重复调用相当于单个调用，并且所有参数都连接在一起。
 - digest() ：返回到目前为止传递给update（）方法的字节的摘要。就是hash算法处理后的结果
 - hexdigest():像digest（）一样，但摘要是作为双倍长度的unicode对象返回的，只包含十六进制数字。
 - copy(): 返回哈希对象的副本（克隆）。 
'''

m = hashlib.md5()  # 选择使用md5加密

m.update("wuwenda".encode("utf-8"))
print(m.hexdigest())
m.update("123".encode("utf-8"))
print(m.hexdigest())

m1 = hashlib.md5()
m1.update("wuwenda123".encode("utf-8"))   # 分开两次调用，和直接拼接调用，加密结果是一样的
print(m1.hexdigest())


