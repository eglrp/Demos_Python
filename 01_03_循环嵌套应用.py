# -*- coding: UTF-8 -*-

n = 100  # 要找的范围

i = 2
while (i < n):
    j = 2
    while j <= i / j:
        if not (i % j):
            break
        j += 1
    if j > i / j:
        print i, " 是素数"
    i += 1

print "Good bye!"

# continue语句用法
for letter in 'Python':  # 第一个实例
    if letter == 'h':
        continue
    print '当前字母 :', letter

var = 10  # 第二个实例
while var > 0:
    var -= 1
    if var == 5:
        continue
    print '当前变量值 :', var
print "Good bye!"
