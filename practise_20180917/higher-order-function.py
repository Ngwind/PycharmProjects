from functools import reduce
'''
高阶函数练习
编写高阶函数，就是让函数的参数能够接收别的函数。
把函数作为参数传入，这样的函数称为高阶函数，函数式编程就是指这种高度抽象的编程范式。
学习系统内建的几个高阶函数
- map()
- reduce()
- filter()
- sorted()
'''

# map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
# 例如用map函数实现：把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
in_put = ['adam', 'LISA', 'barT']
out_put = map(str.capitalize, in_put)
print("map():\n", list(out_put))

# reduce()把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce()把结果继续和序列的下一个元素做累积计算
# 即reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
# 例如把序列[1, 3, 5, 7, 9]变换成整数13579
r_in_put = [1, 3, 5, 7, 9]


def f(a,b):
    return a*10+b


r_out_put = reduce(f, r_in_put)
print("reduce():\n", r_out_put)

# 和map()类似，filter()也接收一个函数和一个序列。
# 和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
# 例如找出100以内能被3整除的数
f_in_put = range(100)
f_out_put = filter(lambda x: x % 3 == 0, f_in_put)
print("filter():\n", list(f_out_put))

# sorted()函数可以对list进行排序。sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序。
# 例如按绝对值大小排序
s_in_put = [36, 5, -12, 9, -21]
s_out_put = sorted(s_in_put, key=abs)
print("sorted():\n", s_out_put)
