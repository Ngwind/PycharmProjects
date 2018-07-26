str = 'hello world!'
str = str.capitalize()#  大写字符串第一个字符
print(str)

str = 'HELLO world! βαλß'
str1 = str.casefold()# 把大写字母转化为小写，包块除了英语字母外的其他字母（如拉丁文）
print(str1)
str2 = str.lower()#  把所有大写字母转换成小写，英文字母
print(str2)

str = 'hello world!'
str = str.center(90, '+')# 在90个字符位置中，让字符串居中，并且用+号填充其余空白位置
print(str)
str_ljust = "dear xxx:"
print(str_ljust.ljust(30, '='))# 在90个字符位置中，让字符串靠左，并且用=号填充其余空白位置

str = 'hello hello hello hello hello hello hello hello'
str = str.count('hell', 12, 18)
print(str)

str = "y name is {0}"
print(str.format("3"))

str1 = '-'
l = ['a', 'b', 'c']
print(str1.join(l))#  把str1作为分隔符,隔开l中的每一个元素

str_lstrip = "888d hello world"
print(str_lstrip.lstrip('8'))#去除字符串左边的8字符

str_partition = "abcdefghijklmn"
print(str_partition.partition("efg"))#  在字符串中查找efg的位置，返回一个三元组。

str_replace = "ac ac ac have show three times?"
print(str_replace.replace('ac', 'tom', 2))#  用制定字符串tom代替ac，次数为2次

# dict_format = ["xx", "sa", "bb"]
# print("there are {0},{1},{2}".format(dict_format))

str_split = "hello world，hello world，hello world，hello world"
print(str_split.split("ll", 1))# 把ll作为分隔切片，返回被ll切开的元组（参数1代表只用第一个出现的ll作为分隔切片）

str_in = "abcde"
str_out = "12345"
print("see this!")
print(str)
print(str.maketrans(str_in, str_out, "fghp"))
print(str)
print("qwertyuiop".translate(str.maketrans(str_in, str_out, "fghp")))# 替换字符串的字符，fghp为删除的字符


str_zfill = "-67.9"
print(str_zfill.zfill(8))#把字符串扩展为8个字符长度，不够的地方用0（zero）补充，但是会在-/+后面开始补充
