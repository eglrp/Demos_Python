# -*-coding:UTF-8 -*-
import random
import numpy as np
import matplotlib.pyplot as plt


# 生成矩阵的方法:
# np.ones()
# np.eye()
# np.identity()
# np.zeros_like()
# np.empty_like()
# np.ones_like()
# np.full_like()
# np.diag((1, 3, 4))

a = np.array([[1, 2, 3], [4, 5, 6]])

# 矩阵的属性
print a.ndim  # 2 2维矩阵
print a.T # 转置
print a.transpose() # 和.T一样，只是可以指定axes
print a.shape  # 行数，列数


print np.sum(a)  # 输出是直接一个数,若用
print np.sum(a, axis=0)  # axis=0按列相加
print np.sum(a, axis=1, keepdims=True)  # axis=1按行相加,输出保持为列向量,keepdims了后就和matlab里的sum一样了,加出来该是行向量就是行向量，该是列向量就是列向量
print np.shape(np.sum(a))  # 一个数则不具有tuple的shape了 输出()
print sum(a)  # 系统自带的sum,输出按列相加,为一个一维数组
print np.shape(sum(a))  # 输出(3L,)

a1 = np.arange(10).reshape((2, 5))  # -1，表示自己计算
a1 = a1.reshape(-1, 2)  # 就成了 5,2了
print a1
print np.argmax(a1, axis=0)  # 取最大值的索引
print np.argmax(a1, axis=1)

a = np.array([[1, 2, 3], [1, 0, 1], [2, 3, 4], [4, 4, 5]])
print a.flatten()  # 矩阵转向量
print a.flatten().reshape((2, 6))

a = np.array([[0, 1, 0, 2, 0, 3], [0, 1, 0, 2, 0, 3]])
print np.flatnonzero(a)  # 1,3,5,7,9,Return indices that are non-zero in the flattened version of a.

print (a1 > 5)
print (a1 != 0)
c = np.nonzero(a1 > 5)
print c
print type(c)  # tuple ，不如用(a1!=0)

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print np.delete(arr, 1, 0)  # 1表示下标为1,0表示行
print np.delete(arr, 2, 1)  # 2表示下标为2,1表示列
print np.delete(arr, [1, 2], 0)  # 删除两行

a = np.array([1, 2, 3])
b = np.array([2, 3, 4])
print np.abs(a - b)  # [1,1,1]

c = np.abs(a - b) != 0
print c
print np.sum(c)  # True 的值是1 ，相加就是3
print int(False)  # 0
print int(True)  # 1

a = np.array([[1, 2, 3], [2, 3, 4]])
b = np.array([[2, 3, 4], [5, 6, 7]])
print np.square(a[1, :], b[1, :])  # 把第一个参数平方到第二个参数，第二个参数是out,可以看到b被改变了，本身也有输出虽然
print b

a = np.array([[1, 2, 3], [1, 0, 1], [2, 3, 4], [4, 4, 5]])
print a[0:1]  # 第一行

# print range(start=10,stop=20)
print np.arange(start=1, stop=100, step=10, dtype='float')  # 和内置的range不一样的是，第二个参数是stop

a = np.arange(1, 10)
print a[-1::-1]  # start stop step ,-1代表最后一个，-1 代表向前一步
print a[1: 8: 2]  # 2 4 6 8

u = np.linspace(start=-1, stop=1.5, num=50)  # linspace demo