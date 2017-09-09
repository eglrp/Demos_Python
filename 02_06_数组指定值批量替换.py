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

# im = pimg.open('07_up_045_RCC.png')
# im1 = np.array(im, dtype='uint8')
# print im1.shape
# plt.imshow(im1)
# im = pimg.open('2007_000032.png')
# im1 = np.array(im, dtype='uint8')
# print im1.shape
# plt.figure()
# plt.imshow(im1)
# plt.show()

# src = 'I:\\My Documents\\My Desktop\\4class_0_125_src_RCC\\rcc_val'
# dst = 'I:\\My Documents\\My Desktop\\4class_0_125_src_RCC\\rcc_val_label_refine'
# files = os.listdir(src)
# files.sort()
#
# for file in files:
#     im = plt.imread(os.path.join(src, file))
#     im_refine = np.zeros((im.shape[0], im.shape[1], 3,), dtype='uint8')
#     idx = im == [1.0]
#     im_refine[idx, :] = [128, 0, 0]
#     im_pil = pimg.fromarray(im_refine)
#     im_pil.save(os.path.join(dst, file))
#     # cv2的imwrite压根保存出来就是错的,
#     # plt.imsave保存三通道的png图像会自动变成4通道，
#     # 真是B了狗了，最后还是PIL的才正常
#     # 不过这样在读入进来貌似数据还是有差距？
#


src = 'I:\\My Documents\\My Desktop\\4class_0_125_src_RCC\\rcc_train'
dst = 'I:\\My Documents\\My Desktop\\4class_0_125_src_RCC\\rcc_train_label_refine'
files = os.listdir(src)
files.sort()

for file in files:
    im = pimg.open(os.path.join(src, file))
    im_np = np.array(im, dtype='uint8')
    im_refine = np.zeros((im_np.shape[0], im_np.shape[1]), dtype='uint8')
    idx = im_np == 255
    im_refine[idx] = 1  # 把255换成1
    im = pimg.fromarray(im_refine)
    im.save(os.path.join(dst, file))
