import shutil
import os
import fnmatch
os.chdir(r'/audio')
目录列表 = os.listdir(r'/audio')
for 文件名 in 目录列表:
    if fnmatch.fnmatch(文件名, '女神的贴身高手*'):  # 匹配模式为星号，表示任意的字符。当fnmatch.fnmatch(文件名, '*.txt')返回True时，执行下方缩进代码块
        l = 文件名.split(' ')
        num = l[1]
        name = l[2].split('（')[0]
        title = num + ' ' + name + '.m4a'
        os.rename(文件名, title)