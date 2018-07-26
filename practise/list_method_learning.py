list_test = ["aaa", "bbb", "ccc"]
print(list_test)

list_test.append("ddd")
print(list_test)

list_test.clear()
print(list_test)

list_copy = list_test.copy()
print(list_copy)

list_test = ["aaa", "bbb", "ccc"]
print(list_test.count('bbb'))

list_test.extend(["sdf", "asdfs", 1, 3, ["dgf", "sffs"]])
print(list_test)

list_test.extend(list_test)
print(list_test)
# 删
list_copy = ["a", "b", "c", "d", 1, 2]
list_test.pop()
print(list_test)
list_test.remove("aaa")
# 查
print("list_test的内容为:\n", list_test)
for i in list_test:
    if i == "bbb":
        continue
    else:
        print(i, end=",")
print()
print("[", end="")
for k in range(len(list_test)):
    print("'", list_test[k], "'", end=",", sep="")
print("]")

