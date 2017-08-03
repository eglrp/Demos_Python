# -*- coding:UTF-8 -*-

numbers = [12, 13, 12, 15, 12, 15, 16]
print len(numbers)
even = []
odd = []

while (len(numbers) > 0):
    number = numbers.pop()
    if (number % 2 == 0):
        even.append(number)
    else:
        odd.append(number)

print 'even:'
print even
print 'odd'
print odd

# continue 和 break 用法
i = 1
while i < 10:
    i += 1
    if i % 2 > 0:  # 非双数时跳过输出
        continue
    print i,  # 输出双数2、4、6、8、10
print

i = 1
while 1:  # 循环条件为1必定成立
    print i,  # 输出1~10
    i += 1
    if i > 10:  # 当i大于10时跳出循环
        break
print

var = 1
while var == 1:  # python的while可以接else
    num = raw_input('please enter a even number:')  # raw_input返回的是文本型
    print 'your input is:', num
    if int(num) % 2 != 0:
        var = 2
else:
    print 'you entered a odd number'
    print 'good bye'
