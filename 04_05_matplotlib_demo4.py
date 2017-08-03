# coding:UTF-8
import numpy as np
import matplotlib.pyplot as plt
import cv2

lena = plt.imread('../lena.jpg')
val, mask = cv2.threshold(lena, 100, 255, type=cv2.THRESH_BINARY)
# 返回值有两个，一个是阈值，一个是阈值化后的图像
print mask.shape
# lena = lena.astype('float')
# lena *= 0.5
plt.figure()
plt.imshow(mask)
plt.show()
# plt.figure()
# plt.imshow(lena.astype('uint8'))
# plt.axis('off')
# plt.show()
