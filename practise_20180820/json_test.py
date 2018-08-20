import json

'''
json模块的练习代码
json模块主要函数是dump和load，分别是编码和解码。
'''

print(json.dumps({"1":2,"3":4,5:[3,15,345]},indent=4))
