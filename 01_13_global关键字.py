# -*- coding:UTF-8 -*-

# 具体参考https://www.cnblogs.com/lytwajue/p/7324724.html
COUNT = 1


def func():
    global COUNT  # 加了这个才能找到
    COUNT += 1  # 报错，找不到COUNT的定义


func()
print COUNT
