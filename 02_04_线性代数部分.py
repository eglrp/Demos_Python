# coding:UTF-8
import numpy as np

a = np.array([[1, 2, 3, 4], [2, 3, 4, 5]])
print np.mean(a, axis=1)
b = np.cov(a)  # 和matlab的不一样，前面系数是 1/n,matlab是1/(n-1)
print a
print b

c = np.linalg.inv(a)  # 逆矩阵
print c

U, S, Vh = np.linalg.svd(a)  # 奇异值分解
print '\n'
V = Vh.T
print U
print '\n'
print S
print '\n'
print V
