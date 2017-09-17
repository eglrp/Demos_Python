# coding:UTF-8
import numpy as np
import random

"""
rand(d0, d1, ..., dn)	Random values in a given shape.
randn(d0, d1, ..., dn)	Return a sample (or samples) from the “standard normal” distribution.
randint(low[, high, size, dtype])	Return random integers from low (inclusive) to high (exclusive).
random_integers(low[, high, size])	Random integers of type np.int between low and high, inclusive.
random_sample([size])	Return random floats in the half-open interval [0.0, 1.0).
random([size])	Return random floats in the half-open interval [0.0, 1.0).产生随机矩阵，如random.random([2,3])产生一个2x3维的随机数
ranf([size])	Return random floats in the half-open interval [0.0, 1.0).
sample([size])	Return random floats in the half-open interval [0.0, 1.0).
choice(a[, size, replace, p])	Generates a random sample from a given 1-D array
bytes(length)	Return random bytes.
"""

print np.random.rand(3, 4)  # 普通随机数float,3x4
print np.random.randn(10)  # 10个元素的一维数组，不是1x10的行向量
assert (np.random.rand(1, 5).shape == (1, 5))  # 这种写法才是行向量
print np.random.randn(10, 2)  # 10x2的数组

print np.random.random((1, 10))  # 1x 10
print np.random.random_integers(0, 10, 5)  # deprecated,use randint
print np.random.randint(0, 10, 10)  # 0-10, 10个元素
print np.random.randint(0, 10, (2, 2))  # 0-10, 2x2的矩阵

a = np.random.randn(10)
b = random.sample(a, 5)  # 从10个元素中随机选5个

print np.random.sample((2, 2))  # 其实就是返回[0-1]的随机数

"""
    random_sample(size=None)

            Return random floats in the half-open interval [0.0, 1.0).

            Results are from the "continuous uniform" distribution over the
            stated interval.  To sample :math:`Unif[a, b), b > a` multiply
            the output of `random_sample` by `(b-a)` and add `a`::

              (b - a) * random_sample() + a

            Parameters
            ----------
            size : int or tuple of ints, optional
                Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
                ``m * n * k`` samples are drawn.  Default is None, in which case a
                single value is returned.

            Returns
            -------
            out : float or ndarray of floats
                Array of random floats of shape `size` (unless ``size=None``, in which
                case a single float is returned).
"""
a = np.random.randn(6)
print a
print np.random.choice(a, (2, 2), replace=True)  # choice从一维的里面取指定size的随机 ,replace参数不是决定可以重复否的，最后一个参数可以指定一个概率，即各项被选中的概率
# 可以用random.sample替代


mean = [0, 0]  # 均值
cov = [[1, 0], [0, 100]]  # 协方差矩阵
x, y = np.random.multivariate_normal(mean, cov, 500).T  # 生成指定均值和方差的正态分布矩阵

print np.random.randint(92, 95, (80), 'uint8')
