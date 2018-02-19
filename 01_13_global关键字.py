# -*- coding:UTF-8 -*-

# 具体参考https://www.cnblogs.com/lytwajue/p/7324724.html



def func():
    global COUNT  # 加了这个才能找到,指定了global的话，在此声明前就不能使用这个变量
    print(COUNT)  # 不赋值(修改)的话是能够使用的

    COUNT += 1  # 报错，找不到COUNT的定义

COUNT = 1 # 定义的位置在前在后无所谓，但是函数内部，global一定要在最前

func()
print COUNT
