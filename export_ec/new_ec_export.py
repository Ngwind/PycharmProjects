import os
import subprocess
import time
"""
这个脚本用来导出手机中的ec文件到电脑，
使用exist方法直接判断完整路径，
代替之前的每一级判断一次
"""

"""
=========================配置参数==================================
"""
# 手机id
phone_id_dir = ""
# 用户名
user_name = "吴文达"

# 局域网映射地址
net_file_location = "z:"

# 手机的ec文件地址
phone_file_location = "/sdcard/hago_coverage/1_6_8/"

# 电脑的ec文件存放地址
pc_file_location = "D:/Users/Administrator/Desktop/代码覆盖率"

# 本次测试的模块
test_model = "首页"

# p1还是p2部分的用例
m_part = "p1"

# 日期格式的文件夹
# 本地日期文件夹2018-11-19
pc_date_dir = time.strftime("%Y-%m-%d", time.localtime(time.time()))
# 局域网日期文件夹1119
net_date_dir = time.strftime("%m%d", time.localtime(time.time()))

print("当前日期:"+pc_date_dir)
print("======当前配置======")
print("用户名：", user_name)
print("局域网映射地址:", net_file_location)
print("手机的ec文件地址:", phone_file_location)
print("电脑的ec文件存放地址:", pc_file_location)
print("本次测试的模块:", test_model)
print("p1还是p2部分的用例:", m_part)
check_str = input("确认无误？[y/n]")
if check_str == "y":
    print("开始执行脚本：")
else:
    os.system(r"start E:\github_reository\PycharmProjects\export_ec\new_ec_export.py")
    exit()
""" ====================================================================
判断手机连接情况
连接成功则获取手机id号
"""
os.system("adb version")
popen_phone = subprocess.Popen("adb devices", stdout=subprocess.PIPE, shell=True)
popen_phone.wait()
phone_id = popen_phone.stdout.read().decode(encoding="utf-8")

for i in range(1, 4):
    print("等待"+str(i)+"秒")
    time.sleep(1)
print(phone_id)
if phone_id == "List of devices attached \r\n\r\n":
    print("连接失败!")
    input("输入enter退出...")
    exit()
else:
    # 手机id号文件夹
    phone_id_dir = phone_id.split(sep='\t')[0].split(sep='\n')[1]

"""
=====================================================================
手机连接成功，
判断本地文件夹和局域网文件夹是否已经存在，
若不存在，则创建该文件夹
"""
pc_path = pc_file_location+"/"+pc_date_dir+"/"+test_model+"/"+phone_id_dir
model_name_part = test_model+"_"+user_name+"("+m_part+")"
net_date_path = net_file_location+"/"+net_date_dir+"/"+model_name_part+"/"+phone_id_dir
net_part_path = net_file_location+"/"+m_part+"/"+test_model+"/"+user_name+"/"+phone_id_dir
# 本地文件夹
if not os.path.exists(pc_path):
    os.makedirs(pc_path)
    print("新建路径:"+pc_path)
else:
    print("路径"+pc_path+"已存在")
# 局域网日期文件夹
if not os.path.exists(net_date_path):
    os.makedirs(net_date_path)
    print("新建路径"+net_date_path)
else:
    print("路径" + net_date_path + "已存在")
# 局域网part文件夹
if not os.path.exists(net_part_path):
    os.makedirs(net_part_path)
    print("新建路径"+net_part_path)
else:
    print("路径"+net_part_path+"已存在")

"""
=====================================================================
传输手机ec文件到pc端
本地文件夹
局域网date文件夹
局域网part文件夹
然后删除手机ec文件
"""

# 开始传输ec文件--->本地文件夹
print("开始传输ec文件--->本地文件夹")
popen_pc = subprocess.Popen("adb pull "+phone_file_location+" "+pc_path, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
returncode = popen_pc.poll()
while returncode is None:
    line = popen_pc.stdout.readline().decode(encoding="gbk")
    returncode = popen_pc.poll()
    line = line.strip()
    print(line)
print("文件传输完成1")

# 开始传输ec文件--->局域网date文件夹
print("开始传输ec文件--->局域网date文件夹")
popen_net_d = subprocess.Popen("adb pull " + phone_file_location + " " + net_date_path, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
returncode = popen_net_d.poll()
while returncode is None:
    line = popen_net_d.stdout.readline().decode(encoding="gbk")
    returncode = popen_net_d.poll()
    line = line.strip()
    print(line)
print("文件传输完成2")

# 开始传输ec文件--->局域网part文件夹
print("开始传输ec文件--->局域网part文件夹")
popen_net_p = subprocess.Popen("adb pull " + phone_file_location + " " + net_part_path, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
returncode = popen_net_p.poll()
while returncode is None:
    line = popen_net_p.stdout.readline().decode(encoding="gbk")
    returncode = popen_net_p.poll()
    line = line.strip()
    print(line)
print("文件传输完成3")

# 清除手机文件
os.system("adb shell rm "+phone_file_location+"*")
print("已清除原ec文件")
print("打开："+pc_path)
print("打开："+net_date_path)
print("打开："+net_part_path)

os.system("start "+pc_path)
os.system("start "+net_part_path)
os.system("start "+net_date_path)
print("执行完成！")
