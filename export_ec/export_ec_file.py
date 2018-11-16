import os
import subprocess
import time
"""
这个脚本用来导出手机中的ec文件到电脑
"""
"""
配置参数：
"""
phone_file_location = "/sdcard/hago_coverage/1_6_8"  # 手机的ec文件地址
pc_file_location = "D:/Users/Administrator/Desktop/代码覆盖率/"  # 电脑的ec文件存放地址

"""
程序执行部分
"""
test_model_dir = None
while test_model_dir is None:
    test_model_dir = input("输入测试模块名：")+"/"

os.system("adb version")

# 手机连接情况判断
phone_id = subprocess.Popen("adb devices", stdout=subprocess.PIPE, shell=True).stdout.read().decode(encoding="utf-8")
# print(list(phone_id))
if phone_id == "List of devices attached \r\n\r\n":
    print("连接失败!")
else:
    date_dir = time.strftime("%Y-%m-%d", time.localtime(time.time()))+"/"  # 日期文件夹
    phone_id_dir = phone_id.split(sep='\t')[0].split(sep='\n')[1]+"/"  # 手机id号文件夹
   # print(phone_id_dir)
    print("当前日期:"+date_dir)
    os.chdir(pc_file_location)
    print("当前位置", os.getcwd())

# 创建日期文件夹
    if not os.path.exists(pc_file_location+date_dir):
        os.mkdir(date_dir)
        print("新建文件夹：" + pc_file_location + date_dir)
    else:
        print(pc_file_location + date_dir + "文件夹已存在")

# 创建测试模块文件夹
    if not os.path.exists(pc_file_location+date_dir+test_model_dir):
        os.mkdir(date_dir+test_model_dir)
        print("新建文件夹：" + pc_file_location + date_dir+test_model_dir)
    else:
        print(pc_file_location + date_dir + test_model_dir + "文件夹已存在")

# 创建手机id文件夹
    if not os.path.exists(pc_file_location+date_dir+test_model_dir + phone_id_dir):
        os.mkdir(date_dir+test_model_dir+phone_id_dir)
        print("新建文件夹：" + pc_file_location + date_dir+test_model_dir+phone_id_dir)
    else:
        print(pc_file_location + date_dir + test_model_dir + phone_id_dir + "文件夹已存在")

# 传输文件
    print("开始传输文件")
    os.system("adb pull "+phone_file_location+" "+pc_file_location+date_dir+test_model_dir)
    print("文件传输完成")
    pass

