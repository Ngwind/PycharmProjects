import re

substr = []  # 存放子字符串
i = 0

str_in = input()
if re.match("^[a-z]+$", str_in)==None:
    print(0)
else:
    list_in = list(str_in)
    while i<len(list_in)-1:
        print(list_in[i])
        j = i+1
        while j in range(i + 1, len(list_in)):
            if list_in[i] == list_in[j]:
                j = j + 1
                print(j)
                continue
            else:
                if str_in[i:j] in substr:
                    i=j
                    break
                else:
                    substr.append(str_in[i:j])
                    i=j

print(substr)
#
# a="111"
# for i in range(1,1):
#     print(a[i])