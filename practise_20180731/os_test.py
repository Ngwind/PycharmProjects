import os
import os.path

print(os.path.abspath("test"))  # abspath函数返回path路径的绝对路径
print(os.path.basename("D://aaa/bbb"))  # basename函数返回path路径的最后一级名称。注意:如果路径path以'/'结尾，则返回空
