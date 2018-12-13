import getopt
import sys
import xlrd
import re

# 存放各种括号的列表
chars_config_list = [('{', '}'),
                     ('[', ']'),
                     ('(', ')')]


def check_file_type(e_str):
    """
    检查文件名是否是xls和xlsx格式，返回True或者False
    :param e_str: 文件名字符串
    :return: 匹配则返回True，反之
    """
    p = re.compile("\.(xls|xlsx)$")
    if re.search(p, e_str):
        return True
    else:
        return False


def check_char(chars_list, checked_str):
    """
    判断一个字符串括号是否成对的函数，返回Bool值
    chars_list是一个保存左括号和右括号的list，例如['{','}']
    checked_str 是被检查的字符串
    """
    char_stack = 0
    for c in checked_str:
        if char_stack >= 0 and c == chars_list[0]:
            char_stack += 1
        elif char_stack >= 0 and c == chars_list[1]:
            char_stack -= 1
        elif char_stack < 0:
            return False
    if char_stack != 0:
        return False
    else:
        return True


def split_command(c_str: object):
    """
    把指令差分，使用正则表达式判断指令类型
    分为三种指令：
    1.逗号分隔型
    2.to型
    2.to加not型
    :param c_str:待处理的指令
    :return: 返回处理好的指令元组
    """
    p_1 = re.compile("^add_item(?:\s)+\{\{(?:\s)+(?P<items>\S+)(?:\s)+\}\}$")
    p_2 = re.compile("^add_item(?:\s)+\{\{(?:\s)+(?P<start>\d+)(?:\s)+to(?:\s)+(?P<end>\d+)(?:\s)+\}\}$")
    m_1 = re.match(p_1, c_str)
    m_2 = re.match(p_2, c_str)
    if m_2:
        print("start:"+m_2.group("start"), "end:"+m_2.group("end"))
    elif m_1:
        print("items:"+m_1.group("items"))
    else:
        print("no pattern,error!")


def report_error(sheet, row, col):
    """
    这个函数用来处理检查到单元格有错误之后要做的事
    :param sheet: 工作表名
    :param row: 单元格行
    :param col: 单元格列
    :return:
    """
    print("工作表:{}，第{}行，第{}列有错误！".format(sheet, row, col))
    pass


def sheet_cell(sheet):
    """
    对每个工作表的所有单元格进行检查
    :param sheet: 是一个工作表
    :return: none
    """
    s_row = sheet.nrows
    s_col = sheet.ncols
    for r in range(s_row):
        for c in range(s_col):
            ch_str = str(sheet.cell_value(r, c))
            if not ch_str == '':  # 单元格是空的就不用检查了
                for item in chars_config_list:
                    if not check_char(item, ch_str):
                        report_error(sheet.name, r, c)


def main():
    """
    检查excel文件中每个单元格的内容是否符合要求.
    使用'-h'参数查看帮助
    使用'-f filename'指定xlsx文件路径
    """
    opts, args = getopt.getopt(sys.argv[1:], 'f:h')
    xl = None
    for o, a in opts:
        if o == '-f':
            xl = xlrd.open_workbook(a)
        elif o == '-h':
            print(main.__doc__)
    if xl is None:
        print("未指定文件！请使用参数 '-h' 查看帮助！")
        return
    sheet_list = xl.sheets()
    for s in sheet_list:
        sheet_cell(s)
    pass


if __name__ == "__main__":
    # print(check_file_type(input("input file:")))
    while True:
        split_command(input("input test string:"))
    pass
