
class Person(object):
    sex = "m"
    age = 18
    __birthday = "2018-09-01"

    def __init__(self, name: "名字") -> "Person的构造函数":
        print("init is called")
        self.name = name
        self.food_list = []

    # 类方法，第一个参数是self
    def eat(self, food):
        self.food_list.append(food)
        print("I have eat :", self.food_list)

    def get_birthday(self):
        return self.__birthday

    # 静态方法staticmethod，第一个参数不用使用self，定义时要用@staticmethod修饰
    @staticmethod
    def sing(song):
        print(song)

    # 类方法classmethod，第一个参数不用self而是使用cls，可以直接被类调用，使用是要用@classmethod修饰
    @classmethod
    def run(cls, distance):
        print("我跑了", distance, "m")
    # 属性方法property,把函数变成一个静态属性，调用时不需要（），一般用在不注重过程，只关注结果的情况

    @property
    def get_age(self):
        return print(self.age)

    # 其他的一些内置方法：__new__当新建实例时调用.__str__当输出实例时调用,__del__当销毁实例时调用
    def __new__(cls, *args, **kwargs):
        print("new is called")
        return super(Person, cls).__new__(cls)

    def __del__(self):
        print("del is called")

    def __str__(self):
        print("str is called")
        return self.name


#a = Person(input("输入名字"))  # demo
#print(a.sex)
#
## 输出类变量性别
#print("使用get函数访问私有变量birthday：", a.get_birthday())
#print("使用类名前缀访问：", a._Person__birthday)
#
## 输出私有变量，要使用get函数获取，不能直接访问变量 。但是其实能够使用"_class"+私有变量名访问
#for i in range(3):
#    a.eat(input("输入要吃的食物"))  # 进食
#
## 对象的静态方法演示
#a.sing("生日歌")
#
## 类的类方法演示
#Person.run(100)
#
## 属性方法演示
#a.get_age
#
## 其他内置函数调用演示
#b = Person("xiao_hong")
#print(b)
#del b
#
