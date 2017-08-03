# coding:UTF-8
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 200)

plt.close('all')
plt.figure(1)
plt.subplot(121);
plt.plot(x, np.cos(x), 'r')
plt.subplot(122)
plt.plot(x, np.sin(x), 'g')

mean = [0, 0]
cov = [[1, 0], [0, 100]]  # 协方差矩阵
x, y = np.random.multivariate_normal(mean, cov, 500).T

# print n
plt.figure(2)
plt.plot(x, y, 'x')
plt.axis('equal')

plt.figure(3)
n = np.random.randn(20000)
print np.mean(n)
plt.plot(np.linspace(0, 200, 20000), n, 'gx')
# plt.show()

a = (np.random.randn(300) * 2 + 93).astype('uint8')
plt.figure(4)
print np.mean(a)
plt.bar(np.arange(300), a)


plt.show()

