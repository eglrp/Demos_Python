# -*- coding: UTF-8 -*-

import string

a = "hello world"
print a[0:6] + "aaa"
# \(在行尾时) 	续行符
# \\ 	反斜杠符号
# \' 	单引号
# \" 	双引号
# \a 	响铃
# \b 	退格(Backspace)
# \e 	转义
# \000 	空
# \n 	换行
# \v 	纵向制表符
# \t 	横向制表符
# \r 	回车
# \f 	换页
# \oyy 	八进制数，yy代表的字符，例如：\o12代表换行
# \xyy 	十六进制数，yy代表的字符，例如：\x0a代表换行
# \other 	其它的字符以普通格式输出

print r'\n\r'  # 带r表示不进行转义
print '\n\r'

if 'h' in a:
    print 'h is in a'
else:
    print 'h is not in a'

if 'd' not in a:
    print 'h is not in a'
else:
    print 'h is in a'

print "My name is %s and my age is %d" % ('Bob', 21)

# % c
# 格式化字符及其ASCII码
# % s
# 格式化字符串
# % d
# 格式化整数
# % u
# 格式化无符号整型
# % o
# 格式化无符号八进制数
# % x
# 格式化无符号十六进制数
# % X
# 格式化无符号十六进制数（大写）
# % f
# 格式化浮点数字，可指定小数点后的精度
# % e
# 用科学计数法格式化浮点数
# % E
# 作用同 % e，用科学计数法格式化浮点数
# % g % f和 % e的简写
# % G % f
# 和 % E
# 的简写
# % p
# 用十六进制数格式化变量的地址

print "%+03.2f" % 10.5

print u'Hello World'

_str = 'hello World'
str_u = unicode(_str)
print str_u
print type(_str)  # <type str>
print type(str_u)  # <type 'unicode'>

print string.capitalize(_str)  # 首字母大写

str1 = '2a'
print str1[1].isdigit()  # False
print str1[0].isdigit()  # True
print _str.lower()  # hello world
print _str.upper()  # HELLO WORLD
print max(_str)  # r
print _str.title() + ' is my first program'.title()  # Hello World Is My First Program
print _str.swapcase()  # HELLO wORLD

str2 = 'a1a2a3a4'
print str2.count('a')  # 4


def findindexofstr(str1, ch):
    indexList = []
    index = str1.find(ch)
    while 1:
        index = str1.find(ch, index)
        if index != -1:
            print index
            indexList.append(index)
            index += 1
        else:
            break
    return indexList


b = findindexofstr(str2, 'a')
print 'indexs are', b

# 拼接iterable里面的内容
items = ['ab', 'cd', 'sas']
print ','.join(items)  # ab,cd,sas
