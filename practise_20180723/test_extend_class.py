from practise_20180723.test_class import Person


class Chinese(Person):
    location = "中国"

    def __init__(self, name, chinese_name):
        Person.__init__(self, name)
        self.chinese = chinese_name

    def run(cls, distance):
        print("我跑了", distance, "m--来自重写的run")

# test_package_a


wang = Chinese("wang", "王")
wang.run(100)

