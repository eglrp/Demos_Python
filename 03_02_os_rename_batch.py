# coding:UTF-8
import os


'''
用来重命名一级目录下面按照类别存放各类文件，一类一个文件夹的那种
比如src\\a,src\\b,src\\c,重命名后到dst\\a_001,a_002,b_001,c_002....
'''


src = "I:\\My Documents\\My Desktop\\rocks_resized"
dst = 'I:\\My Documents\\My Desktop\\rocks_renamed'
classfolders = os.listdir(src)

for clsfolder in classfolders:
    files = os.listdir(os.path.join(src,clsfolder))
    files.sort()
    for i, file in enumerate(files):
        old = os.path.join(src, clsfolder, file)
        num = '%03d' % i
        new = os.path.join(dst, clsfolder + '_' + num + os.path.splitext(file)[1])
        print new
        os.rename(old, new)
