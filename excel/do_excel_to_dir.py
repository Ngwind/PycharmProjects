'''
用来批量创建班级综测表的个人文件夹，格式为：学号+姓名
'''


import xlrd
import os
print("读取xlsx")
wb = xlrd.open_workbook('G:\students.xlsx')
sheet1 = wb.sheet_by_name('Sheet1')
print("原始路径：", os.getcwd())
print("开始切换路径...")
os.chdir('G:\大四上学期\大三综测\个人资料')
print("当前路径：", os.getcwd())
i = 0
while i < sheet1.nrows-1:

    dirname = str(int(sheet1.cell(i+1, 0).value)) + sheet1.cell(i+1, 1).value
    print(dirname)
    i += 1
    if os.path.exists('./'+dirname):
        print('file has  been created')
        continue
    else:
        os.mkdir(dirname)
        print('ok')