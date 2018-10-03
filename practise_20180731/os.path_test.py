
import os.path
import time

#  os.path模块常用函数demo:
#  演示用的路径
path = "aaa/bbb/ccc/ddd.py"

#  exists函数判断path是否存在
print(os.path.exists(path))
print(os.path.exists("/aaa/bbb/ccc"))

# abspath函数返回path路径的绝对路径
print(os.path.abspath(path))

# split函数将path拆分成dirname和basename,返回二元元组
print(os.path.split(path))

# dirname函数返回path的目录名
print(os.path.dirname(path))

# filname函数返回path的文件名
print(os.path.basename(path))

# getsize返回文件大小（以字节为单位）
print(os.path.getsize(path))

# getatime, getctime, getmtime三个函数分别返回文件的最后访问、创建、修改时间，path无效则抛出OSError
# 可以使用time.gmtime()来以struct_time形式输出最近修改时间
print(os.path.getatime(path))
print(time.gmtime(os.path.getatime(path)))
print(time.gmtime(os.path.getctime(path)))
print(time.gmtime(os.path.getmtime(path)))

# isabs,isfile,isdir,islink,ismount函数分别判断path是否为绝对路径，常规文件，文件夹，链接，挂载点
print(os.path.isabs(path))
print(os.path.isfile(path))
print(os.path.isdir(path))
print(os.path.islink(path))
print(os.path.ismount(path))

# commonpath函数返回paths参数中，所有路径序列中共有的最长的路径.如果 paths 即包含绝对路径又包含相对路径,或者 paths 为空将抛出ValueError.
print(os.path.commonpath(["/aaa/bbb", "/aaa/bbb/ccc"]))

# commonprefix函数返回list中所有路径的前缀的最长前缀（逐个字符），如果list为空则返回空字串,建议使用commonpath
print(os.path.commonprefix(["/aaa/bbb", "/aaa/bbb/ccc"]))
print(os.path.commonprefix([""]))
print(os.path.commonprefix(["/aaa/bbc", "/aaa/bbb/ccc"]))



