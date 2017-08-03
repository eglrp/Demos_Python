# -*-coding:UTF-8 -*-
from PIL import Image
from PIL import ImageEnhance
from PIL import ImageFilter


im = Image.open("../lena.jpg")
# Image._show(im) # or im.show()
print im.format, im.size, im.mode

# im.show()
# im.save('lena3.jpg')  # 直接在文件名中指定后缀名

# Image.open('lena1.jpg').show()

lena = im.copy()  # 指定ROI
box = (100, 100, 400, 400)
lena_cut = lena.crop(box)
# lena_cut.show()
lena_flip = lena_cut.transpose(Image.ROTATE_180)  # 图像旋转
# lena_flip.show()
lena.paste(lena_cut, box)  # 带Mask的拷贝
# lena.show()


r, g, b = lena.split()
lena_merged = Image.merge("RGB", (r, g, b))  # 顺序不是bgr二是rgb
# lena_merged.show()
# r.show()

lena_resize = lena.resize((180, 180))  # resize
# lena_resize.show()



