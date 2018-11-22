import os
import subprocess
import time
"""
这个脚本用来导出手机中的ec文件到电脑
"""
"""
配置参数：
"""
net_location = "f:"  # 局域网映射地址
user_name = "吴文达"  # 用户名
phone_file_location = "/sdcard/hago_coverage/1_6_8/"  # 手机的ec文件地址
pc_file_location = "D:/Users/Administrator/Desktop/代码覆盖率/"  # 电脑的ec文件存放地址

"""
程序执行部分
"""
m_part = None
test_model_dir = None
while test_model_dir is None or test_model_dir == "" or m_part is None:
    test_model_dir = "和好友玩"
    m_part = "p1"

os.system("adb version")

# 手机连接情况判断
phone_id = subprocess.Popen("adb devices", stdout=subprocess.PIPE, shell=True).stdout.read().decode(encoding="utf-8")
time.sleep(2)
print(phone_id)
if phone_id == "List of devices attached \r\n\r\n":
    print("连接失败!")
    input("输入enter退出...")
    exit()
else:
    date_dir = time.strftime("%Y-%m-%d", time.localtime(time.time()))  # 日期文件夹2018-11-19
    date_dir_net = time.strftime("%m%d", time.localtime(time.time()))  # 日期文件夹1119
    phone_id_dir = phone_id.split(sep='\t')[0].split(sep='\n')[1]  # 手机id号文件夹
#  print(phone_id_dir)
    print("当前日期:"+date_dir)
    print("当前位置", os.getcwd())

# 创建-本地-日期文件夹
    if not os.path.exists(pc_file_location+date_dir):
        os.mkdir(date_dir, mode=775)
        print("新建文件夹：" + pc_file_location + date_dir)
    else:
        print(pc_file_location + date_dir + "文件夹已存在")

# 创建-本地-测试模块文件夹
    if not os.path.exists(pc_file_location+date_dir+test_model_dir):
        os.mkdir(date_dir+test_model_dir, mode=775)
        print("新建文件夹：" + pc_file_location + date_dir+test_model_dir)
    else:
        print(pc_file_location + date_dir + test_model_dir + "文件夹已存在")

# 创建-本地-手机id文件夹
    if not os.path.exists(pc_file_location+date_dir+test_model_dir + phone_id_dir):
        os.mkdir(date_dir+test_model_dir+phone_id_dir, mode=775)
        print("新建文件夹：" + pc_file_location + date_dir+test_model_dir+phone_id_dir)
    else:
        print(pc_file_location + date_dir + test_model_dir + phone_id_dir + "文件夹已存在")

# 传输手机文件到本地电脑
    print("开始传输文件")
    os.system("adb pull "+phone_file_location+" "+pc_file_location+date_dir+test_model_dir+phone_id_dir)
    print("文件传输完成")

# 创建-局域网-日期-个人测试模块文件夹
    if not os.path.exists(net_location + date_dir_net + test_model_dir[0:-1] + "_" + user_name + m_part):
        os.chdir(net_location + date_dir_net)
        os.mkdir(test_model_dir[0:-1] + "_" + user_name + m_part)
    else:
        print(net_location + date_dir_net + test_model_dir[0:-1] + "_" + user_name + m_part+"文件夹已存在")
    if not os.path.exists(net_location + date_dir_net + test_model_dir[0:-1] + "_" + user_name + m_part + phone_id_dir):
        os.chdir(net_location + date_dir_net + test_model_dir[0:-1] + "_" + user_name + m_part[0:-1])
        os.mkdir(phone_id_dir)
        print("新建文件夹：" + os.getcwd()+"/"+phone_id_dir)
    else:
        print(net_location + date_dir_net + test_model_dir + "_" + user_name + m_part + phone_id_dir + "文件夹已存在")

# 传输手机文件到net电脑
    print("开始传输文件")
    os.system("adb pull " + phone_file_location + " " + net_location + date_dir_net + test_model_dir + "_" + user_name + m_part + phone_id_dir)
    print("文件传输完成")


# 清除手机文件
    os.system("adb shell rm "+phone_file_location+"*")
    print("已清除原ec文件")
    os.system("start "+pc_file_location+date_dir)
    input("输入enter退出....")
    pass

