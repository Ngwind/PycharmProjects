def show(*args):
    """
    实现多个参数展示
    :param args:
    :return:
    """
    return print("的show函数输出:", args)



in_put = input("输入参数，以英文逗号隔开:\n")
list_in = in_put.split(",")
print("输入为:", in_put)
print("处理成列表list_in为:", list_in)
print("in_put", end="")
show(tuple(in_put))
print("list_in", end="")
# 解包参数列表
show(*list_in)
# 函数注解


def f(x: "这是输入参数x"=0)->"这是返回值x":
    return print(x)


print(show.__doc__)


print(f.__annotations__)