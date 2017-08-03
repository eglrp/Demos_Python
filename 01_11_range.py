# coding:UTF-8
print range(1, 10)  # 1 to 9
print range(10, 1, -1)  # 10 to 2
print type(range(1, 10))  # 返回一个list
print xrange(1, 10, 2)  # 就输出xrange(1, 10, 2)
for i in xrange(1, 10, 3):  # xrange不保存变量的值
    print i
