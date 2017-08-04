# coding:UTF-8


import os
import numpy as np
import matplotlib.pyplot as plt
import cv2
import PIL.Image as pimg

# 小例子
# a = np.eye(3, 3)
# idx = a == 1.0
# a[idx] = 2.0
# print a

'''
把自己分割得到的0,255的mask转换成voc数据集里面用到的(由标签类别映射)
'''


src = 'I:\\My Documents\\My Desktop\\4class_0_125_src_RCC\\rcc_val'
dst = 'I:\\My Documents\\My Desktop\\4class_0_125_src_RCC\\rcc_val_label_refine'
files = os.listdir(src)
files.sort()

for file in files:
    im = plt.imread(os.path.join(src, file))
    im_refine = np.zeros((im.shape[0], im.shape[1], 3,), dtype='uint8')
    idx = im == [1.0]
    im_refine[idx, :] = [128, 0, 0]
    im_pil = pimg.fromarray(im_refine)
    im_pil.save(os.path.join(dst, file))
    # cv2的imwrite压根保存出来就是错的,
    # plt.imsave保存三通道的png图像会自动变成4通道，
    # 真是B了狗了，最后还是PIL的才正常
    # 不过这样在读入进来貌似数据还是有差距？



