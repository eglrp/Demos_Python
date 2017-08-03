# -*- coding:UTF-8 -*-
import os

print os.curdir  # .
print os.path.curdir  # curdir返回. ，也是相对路径
print os.getcwd()  # getcwd返回绝对路径 用\\带前不带后
print os.path.abspath(os.path.curdir)  # abspath也可以转换相对路径为绝对路径
print __file__  # I:/My Documents/My Desktop/codes/python/Demos_Python/03_01_os_���÷���.py
print os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))  ## 上一级目录路径


print os.pardir  # 当前路径的父目录 ..
print os.path.exists('/home/yang-peng/a.txt')
print os.path.join('\home', 'yang-peng', 'caffe-master', 'a.txt')  # 拼接路径

print os.path.dirname('/home/yang-peng/a.txt')
print os.path.basename('/home/yang-peng/a.txt')
print os.path.basename('/home/yang-peng')  # 结尾带/就不行了


print os.listdir('I:/')  # 注意i:和i:/是不一样的
dir = os.path.join('home', 'yang-peng', 'caffe-master', 'a.txt')
print os.path.splitext(dir)  # 按后缀名分割  # ('home\\yang-peng\\caffe-master\\a', '.txt')
print os.path.split(dir)  # 将文件名和路径分开 # ('home\\yang-peng\\caffe-master', 'a.txt')
