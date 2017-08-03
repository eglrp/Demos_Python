# coding:UTF-8
import cv2
import numpy as np
import os

# 图片resize
# srcdir = 'I:\\My Documents\\My Desktop\\rock_samples\\3dpicture_8\\MidView'  # windows下面最好用\\
srcdir = 'I:\\My Documents\\My Desktop\\rock_samples\\3dpicture_8\\UpView'  # windows下面最好用\\
outdir = os.path.join(srcdir, 'resized')
if (not (os.path.exists(outdir))):
    os.mkdir(outdir)

ratio = 0.125

files = os.listdir(srcdir)
files.sort()
for file in files:
    if (os.path.isfile(os.path.join(srcdir, file)) == False):
        continue
    src = cv2.imread(os.path.join(srcdir, file))
    resized = cv2.resize(src, (int(src.shape[1] * ratio), int(src.shape[0] * ratio)))
    print os.path.join(srcdir, 'resized', file)
    cv2.imwrite(os.path.join(srcdir, 'resized', file), resized)
