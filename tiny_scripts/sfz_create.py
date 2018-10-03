'''
用来生成合法的身份证。根据输入的17位数字，生成第18位校验位
'''

arraydate = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
total = 0
arraym = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']
id_number17 = input('输入身份证前17位：')
if len(id_number17) != 17:
    print('长度不为17！告辞...')
    exit()
else:
    id_n = list(id_number17)
    for i in range(17):
        total = total + arraydate[i]*int(id_n[i])
    m = total % 11
    print("生成身份证：", id_number17+arraym[m])
