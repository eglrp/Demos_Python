# -*- coding: UTF-8 -*-


for letter in 'Python':
    print '当前字母', letter

fruits = {'a', 'b', 'c'}  # 没有:的则是set,不是map
for i in fruits:
    print i

print fruits

fruits = ['banana', 'apple', 'mango']
for index in range(len(fruits)):
    print '当前水果 :', fruits[index]

for idx, fruit in enumerate(fruits):  # enumerate直接就可以用一个计数变量了
    print '当前是第%d个水果:%s' % (idx, fruit)

