# coding:UTF-8
import cv2

src = cv2.imread('../lena.jpg', flags=cv2.CV_LOAD_IMAGE_GRAYSCALE)
# cv2.namedWindow("src", flags=cv2.CV_WINDOW_AUTOSIZE)
# cv2.imshow("src", src)
# cv2.imwrite('lena_gray.jpg', src)

print src.shape  # 读入是numpy的数组，很方便

fliped = cv2.flip(src, 0)  # 其实直接对numpy的array进行翻转操作也可以实现
# cv2.imshow("fliped", fliped)

"""
# Vertical flipping of the image (flipCode == 0) to switch between top-left and bottom-left image origin. This is a typical operation in video processing on Microsoft Windows* OS.
# Horizontal flipping of the image with the subsequent horizontal shift and absolute difference calculation to check for a vertical-axis symmetry (flipCode > 0).
# Simultaneous horizontal and vertical flipping of the image with the subsequent shift and absolute difference calculation to check for a central symmetry (flipCode < 0).
# Reversing the order of point arrays (flipCode > 0 or flipCode == 0).
"""

# 数组分开和合并
splited = cv2.split(src)
print len(splited)  # 3，分别三个通道 ，其实split在Python里面意义不大了，反正都是numpy的array
# cv2.imshow("red", splited[2])
# cv2.imshow("green", splited[1])
# cv2.imshow("blue", splited[0])
merged = cv2.merge((splited[0], splited[1], splited[2]))
# cv2.imshow("merged", merged)
