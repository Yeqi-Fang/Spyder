import os
import glob
import shutil

os.chdir(r'D:\multi_media\DOC\Study')
# print(glob.glob('*.txt'))
# print(glob.glob('孙*.txt'))
# print(glob.glob('孙兴华.分析[0-9].*'))
# print(glob.glob('孙兴华.分析[!0-9].*'))
files = glob.glob('**/*.one', recursive=True)
# print(files)
for file in files:
    # os.rename(文件, )
    newfile = os.path.join(r"D:\multi_media\DOC\Study\笔记", os.path.split(file)[1])
    shutil.copy2(file, newfile)
