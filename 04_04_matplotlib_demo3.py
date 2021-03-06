# -*- coding: UTF-8 -*-
import numpy as np

import matplotlib.pyplot as plt

plt.figure(1)  # 创建图表1

plt.figure(2)  # 创建图表2

ax1 = plt.subplot(221)  # 在图表2中创建子图1

ax2 = plt.subplot(222)  # 在图表2中创建子图2
ax3 = plt.subplot(223)
ax4 = plt.subplot(224)

x = np.linspace(0, 3, 100)

for i in xrange(5):
    plt.figure(1)  # ❶ # 选择图表1

    plt.plot(x, np.exp(i * x / 3))

    plt.sca(ax1)  # ❷ # 选择图表2的子图1

    plt.plot(x, np.sin(i * x))

    plt.sca(ax2)  # 选择图表2的子图2

    plt.plot(x, np.cos(i * x))

plt.figure(3)
i = plt.imread('..\lena.jpg')
print np.shape(i)
plt.imshow(i)

plt.show()
