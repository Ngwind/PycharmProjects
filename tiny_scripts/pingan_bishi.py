str_in = input()
str_num = [0]
for i in str_in:
    i = int(i)
    if i not in str_num:
        str_num.append(i)

str_num.sort()
str_num.reverse()
str_num.remove(0)

sum = 0
for i in range(len(str_num)):
    sum += str_num[i]*(10**i)
print(sum)

