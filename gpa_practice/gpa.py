d_point = []  # 单科成绩列表
d_node = []  # 单科学分列表
num = 0  # 输入科目数


def cal(dp=[], dn=[]):  # 计算绩点的函数
    sum_point_node = 0
    sum_node = 0
    for i in range(len(dp)):
        sum_point_node += (float(dp[i])*float(dn[i]))
        sum_node += float(dn[i])
    return sum_point_node/sum_node


while True:
    num += 1
    point = input("输入第{}科绩点:".format(num))
    node = input("输入第{}科的学分:".format(num))
    d_point.append(point)
    d_node.append(node)
    print("目前绩点为：", cal(dp=d_point, dn=d_node))
    # go_on = input("输入ok结束成绩输入,输入其他任意字符继续成绩输入")
    # if go_on == "ok":
    # break
