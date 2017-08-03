# coding:UTF-8
import cv2
import numpy as np

# 图片resize
src = cv2.imread('../lena.jpg')
resized = cv2.resize(src,
                     (int(src.shape[1] * 0.5), int(src.shape[0] * 0.5)))  # 注意是shape[1]和shape[0],opencv里面行数对应高度和列数对应宽度
print resized.shape

# 滤波函数
blured = cv2.blur(src, (3, 3))
gaussinBlured = cv2.GaussianBlur(src, (3, 3), sigmaX=10)
boxFiltered = cv2.boxFilter(src, -1, (3, 3))

# 色彩空间转换
grayed = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
lab = cv2.cvtColor(src, cv2.COLOR_BGR2LAB)

print np.max(lab[:, :, 0])
print np.min(lab[:, :, 0])
print np.max(lab[:, :, 1])
print np.min(lab[:, :, 1])
print np.max(lab[:, :, 2])
print np.min(lab[:, :, 2])  # 可以看到也是归一化到了0-255的

# canny算法
# cv2.imshow("canny", cv2.Canny(src, 100, 200))




cv2.waitKey(0)
