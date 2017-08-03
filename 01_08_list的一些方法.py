# -*- coding: UTF-8 -*-

a = []
a.append((1, '1'))
a.append((2, '2'))
a.append({3: '3'})
print a
print a[0]
print a[0][0], a[0][1]  # a[0]是一个touple,可以继续用下标访问
print type(a[0])
print type(a[2])

print type(a)

a = [1, 2, 3, 4]
print len(a)
for x in a:
    print x,  # 不换行
print  # 换下行
print ['Hi,'] * 4
b = [2, 1]
a.extend(b)
print a  # [1, 2, 3, 4, 2, 1]
a.reverse()
print a  # [1, 2, 4, 3, 2, 1]
a.sort(reverse=True)
print a  # [4, 3, 2, 2, 1, 1]
print max(a)  # 4
