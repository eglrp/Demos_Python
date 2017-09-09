# coding:UTF-8
import cv2

src = cv2.imread('../lena.jpg')

cv2.imshow('lena', src)

# 四个参数分别是上 下 左 右
cv2.imshow('pad zero', cv2.copyMakeBorder(src, 4, 4, 4, 4, cv2.BORDER_CONSTANT, value=0))
cv2.imshow('pad reflect', cv2.copyMakeBorder(src, 40, 40, 0, 0, cv2.BORDER_REFLECT, value=0))  # reflect 是把边界反向复制
cv2.imshow('pad replicate', cv2.copyMakeBorder(src, 40, 40, 20, 0, cv2.BORDER_REPLICATE, value=0))  # REPLICATE 是把边界直接复制
cv2.imshow('pad ISOLATED', cv2.copyMakeBorder(src, 40, 40, 20, 0, cv2.BORDER_ISOLATED))  # ISOLATED 和constant一样
cv2.waitKey(0)
