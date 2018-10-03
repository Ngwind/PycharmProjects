import os
import stat
#  演示用的路径
path = "aaa/bbb/ccc/ddd.py"

#  os.name表示当前系统名：
print(os.name)

#  查看环境变量。environ是一个mapping类型对象，保存了所有环境变量。
print(os.environ)
#  例如使用environ["homepath"]查看主目录名称
print(os.environ['homepath'])
print(os.environ['classpath'])

#  文件和目录类函数

#  1.access来判断对path的权限（存在F_OK、可读R_OK、可写W_OK、可执行X_OK）
print(os.access(path, os.F_OK))
print(os.access(path, os.R_OK))
print(os.access(path, os.W_OK))
print(os.access(path, os.X_OK))

#  2.chdir更改当前目录为path
#  使用getcwd得到当前工作目录
print(os.getcwd())
os.chdir(path+"/../")
print(os.getcwd())

#  3.chmod更改
#  虽然Windows支持 chmod()，但只能使用它设置文件的只读标志（通过 stat.S_IWRITE 和 stat.S_IREAD 常量或相应的整数值）。所有其他位被忽略。
os.chdir("../../../")
os.chmod(path, 775)
print(os.access(path, os.F_OK))
print(os.access(path, os.R_OK))
print(os.access(path, os.W_OK))
print(os.access(path, os.X_OK))

#  chroot
#  4.chown改变文件/文件夹的所有者/组
#  os.chown()

#  5.listdir展示path路径的文件
print(os.listdir("./"))

#  6.mkdir新建一个文件夹。如果存在则会报错
os.mkdir("test_mkdir", 775)
print(os.listdir("./"))

#  7.makedirs递归目录新建功能。
os.makedirs("./kkk/fff/cc")

#  8.rmdir删除空目录
os.rmdir("test_mkdir")

#  9.removedirs递归删除空目录
os.removedirs("./kkk/fff/cc")

#  10.removedirs递归删除空目录
#  if not (os.path.exists("eee.py")):
#    os.mkdir("eee.py")
#  else:
#    os.rename("eee.py", "ddd.py")
#  system执行一个系统命令
#  os.system("ipconfig")
#  os.system("dir")

with os.scandir("./") as it:
    for entry in it:
        if not entry.name.startswith('.') and entry.is_file():
            print(entry.name)

print(os.system("ping www.baidu.com"))
