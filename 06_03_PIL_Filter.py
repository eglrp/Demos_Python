#coding:UTF-8
from PIL import Image
from PIL import ImageEnhance
from PIL import ImageFilter

lena = Image.open('../lena.jpg')
lena_smooth = lena.filter(ImageFilter.SMOOTH)
# lena_smooth.show()

lena_edgeEnhance = lena.filter(ImageFilter.EDGE_ENHANCE)
# lena_edgeEnhance.show()

lena_gaussianBlur = lena.filter(ImageFilter.GaussianBlur(radius=1))
# lena_gaussianBlur.show()

enh = ImageEnhance.Contrast(lena)
# enh.enhance(1.3).show("30%")
sharpness = ImageEnhance.Sharpness(lena)
# sharpness.enhance(3).show()
# cl = ImageEnhance.Color
# print cl.__doc__

lena_L = lena.convert('L')  # 转换为灰度图
# lena_L.show()

# pt1 = lena.point((1, 1))

print type(lena)

# lena_composite = Image.composite(lena_gaussianBlur, lena_smooth, )
# lena_composite.show()

lena_canny = lena_L.filter(ImageFilter.FIND_EDGES)
lena_canny.show()
print type(lena_canny)
