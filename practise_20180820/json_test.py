import json
'''
json模块的练习代码。
json模块主要函数是dumps和loads，分别是编码和解码。
如果要处理的是文件而不是字符串，你可以使用 json.dump() 和 json.load() 来编码和解码JSON数据
'''
'''
def dumps(obj, *, skipkeys=False, ensure_ascii=True, check_circular=True,
        allow_nan=True, cls=None, indent=None, separators=None,
        default=None, sort_keys=False, **kw):
        
def dump(obj, fp, *, skipkeys=False, ensure_ascii=True, check_circular=True,
        allow_nan=True, cls=None, indent=None, separators=None,
        default=None, sort_keys=False, **kw):
'''
dict_test = {"name": "wd", "age": 11, "sex": "man"}  # python的字典数据类型
json_dumps = json.dumps(dict_test)  # dumps函数把python的dict类型转换成json字符串变量
print(json_dumps)  # 打印json字符串变量的内容
print(type(json_dumps))  # 打印json字符串变量的数据类型（str）
with open("test.json", 'w+') as f:  # 打开json文件用于写入json数据
    json.dump(dict_test, f)  # dump函数把python的dict类型转换成json字符串，并且写入数据到json文件
    print(f.seek(0))  # 把文件指针设置为开头
    print(f.read())  # 读取文件内容

'''
def loads(s, *, encoding=None, cls=None, object_hook=None, parse_float=None,
        parse_int=None, parse_constant=None, object_pairs_hook=None, **kw):
        
def load(fp, *, cls=None, object_hook=None, parse_float=None,
        parse_int=None, parse_constant=None, object_pairs_hook=None, **kw):
'''
json_test = '{"name": "wd", "age": 11, "sex": "man"}'  # json字符串
dict_loads = json.loads(json_test)  # loads函数把json字符串转化为对应的python数据类型
print(dict_loads)  # 打印dict内容
with open("test.json", 'r+') as f:  # 打开json文件
    dict_load = json.load(f)  # load函数读出json文件中的数据，并且转换成dict数据类型变量
    print(type(dict_load))  # 打印dict_load类型
    print(dict_load)  # 打印dict变量内容
