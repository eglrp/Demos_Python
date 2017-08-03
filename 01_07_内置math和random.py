# -*- coding: UTF-8 -*-
import math
import random

a = 2.5
print math.ceil(a)
print math.floor(a)
print round(a)

# python的种子是自动选择的
print random.random()
print random.uniform(1, 10)

a = math.pi
print a
print math.degrees(a)  # 弧度、角度转换
print math.radians(math.degrees(a))

a, b = 3.0, 4.0
print math.hypot(a, b)  # 求三角形的斜边

print math.e
