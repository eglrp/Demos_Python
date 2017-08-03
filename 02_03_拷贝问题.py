# coding:UTF-8

import numpy as np

"""拷贝问题"""
d = np.array([[1], [2], [3]])
d_ShallowCopy = d
d_DeepCopy = d.copy()  # 深拷贝
d_ShallowCopy[0, 0] = 11
d_DeepCopy[1, 0] = 22
print d_ShallowCopy
print d_DeepCopy
print d  # 两个都变了，说明是浅拷贝

d1 = np.array([1, 2, 3])
d_singleCopy = d1[0]
d_singleCopy = 2
print d1  # 1 2 3 ，说明单元素拷贝是深拷贝
