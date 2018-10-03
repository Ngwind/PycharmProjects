'''
根据姓名查找学号
后续希望能实现根据名字首字母查找
'''
import xlrd
print('欢迎使用 根据姓名查找学号')
while 1 :
    name = input("输入姓名：")
    wb = xlrd.open_workbook('G:\students.xlsx')
    sheet = wb.sheet_by_name('Sheet1')
  #  print("你输入了：", name)
    for i in range(sheet.nrows-1):
        # print("对比：",sheet.cell(i+1, 1).value, '格式：', sheet.cell_type(i+1, 1))
        if name == sheet.cell(i+1, 1).value:
            print("他/她的学号：", str(int(sheet.cell(i+1, 0).value)))
            break
        else:
            if i == sheet.nrows-2:
                print("没有找到！")