# -*- coding: UTF-8 -*-
counter = 100
miles = 100.0
name = 'John'

a = b = c = 1
a, b, c = 1, 2, 'John'

# Python有五个标准的数据类型：
#
#     Numbers（数字）
#     String（字符串）
#     List（列表）
#     Tuple（元组）
#     Dictionary（字典）
# Python支持四种不同的数字类型：
#
#     int（有符号整型）
#     long（长整型[也可以代表八进制和十六进制]）
#     float（浮点型）
#     complex（复数）

a = 1
del a  # 删除a的定义，再用的话会提示undefined
# print a

# python的字串列表有2种取值顺序:
#
#     从左到右索引默认0开始的，最大范围是字符串长度少1
#     从右到左索引默认-1开始的，最大范围是字符串开头

a = 'John'
print a.__len__()  # 或者len(a)

for i in range(0, a.__len__(), 1):
    print a[0:i + 1]

for i in range(a.__len__(), 0, -1):
    # print a[-1:i]
    print i

# list例子
_list = ['runoob', 786, 2.23, 'john', 70.2]
tinylist = [123, 'john']

print _list  # 输出完整列表
print _list[0]  # 输出列表的第一个元素
print _list[1:3]  # 输出第二个至第三个的元素
print _list[2:]  # 输出从第三个开始至列表末尾的所有元素
print tinylist * 2  # 输出列表两次
print _list + tinylist  # 打印组合的列表

# 元祖例子（元组不能二次赋值，相当于只读列表。）
_tuple = ('runoob', 786, 2.23, 'john', 70.2)
tinytuple = (123, 'john')

print _tuple  # 输出完整元组
print _tuple[0]  # 输出元组的第一个元素
print _tuple[1:3]  # 输出第二个至第三个的元素
print _tuple[2:]  # 输出从第三个开始至列表末尾的所有元素
print tinytuple * 2  # 输出元组两次
print _tuple + tinytuple  # 打印组合的元组

_tuple = ('runoob', 786, 2.23, 'john', 70.2)
_list = ['runoob', 786, 2.23, 'john', 70.2]
# tuple[2] = 1000    # 元组中是非法应用
_list[2] = 1000  # 列表中是合法应用

# dict例子
print '-----------------------------'
_dict = {1: 2, '3': 4}
print _dict[1]
_dict['key1'] = 'key1_value'  # 可以直接没有这个键的时候直接赋值会新增
print _dict['key1']
for key in _dict.keys():
    print key, ':', _dict[key]

for key, value in _dict.items():  # 也可以这样,items是一个list
    print key, ':', value

exit()
# 三种不同数组分别用[],(),{}初始化,但是都用[]访问

_dict = {}
_dict[1] = 'one'
_dict['two'] = 2
print _dict
tinydict = {'name': 'John', 'code': 20}
print tinydict
print tinydict.keys()
print tinydict.values()

a = 2
print a
print str(a)
print long(a)
