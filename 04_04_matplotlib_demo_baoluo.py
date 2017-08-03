# -*- coding: UTF-8 -*-
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 50, 500)
x = np.exp(-t / 10) * np.cos(t * np.pi / 3)
hx, = plt.plot(t, x)
h1, = plt.plot(t, np.exp(-t / 10), '--')
h2, = plt.plot(t, -np.exp(-t / 10), '--')
plt.legend([hx, h1, h2], ['exp(-t / 10)*cos(t *pi / 3)', 'exp(-t / 10)', '-exp(-t/10)'])
plt.title('testBaoluo')
plt.show()
print t.shape  # 成员不能带括号,不是方法
