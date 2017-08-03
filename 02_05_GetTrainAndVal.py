# -*-coding:UTF-8-*-
import numpy as np
import random
import os

'''
    把src目录下文件按照比例分为两部分，一部分train,一部分val
'''

src = 'E:/Saliency_WorkDir/4class_0_125_src_RCC/SRC'

dst_val = 'E:/Saliency_WorkDir/4class_0_125_src_RCC/val'
dst_tr = 'E:/Saliency_WorkDir/4class_0_125_src_RCC/train'

trainRatio = 0.85

files = os.listdir(src)
files.sort()
num = len(files)
train_num = int(num * trainRatio)
test_num = int(num * (1 - trainRatio))
print 'train_set num:', train_num
print 'val_set num:', test_num
index = np.arange(num)
index_train = random.sample(index, train_num)
# 把train的移走了就剩下val的了
for idx in index_train:
    os.rename(os.path.join(src, files[idx]), os.path.join(dst_tr, files[idx]))
    # os.rename(os.path.join(src1, os.path.splitext(files[idx])[0] + '_RCC.png'),
    #           os.path.join(dst_tr1, os.path.splitext(files[idx])[0] + '_RCC.png'))

    print os.path.join(dst_tr, files[idx])

val_set = os.listdir(src)  # 剩下的就是val
val_set.sort()
for file in val_set:
    os.rename(os.path.join(src, file), os.path.join(dst_val, file))
    # os.rename(os.path.join(src1, os.path.splitext(file)[0] + '_RCC.png'),
    #           os.path.join(dst_val1, os.path.splitext(file)[0] + '_RCC.png'))