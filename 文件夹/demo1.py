import os
# for 元素 in os.scandir('c:/'):
#     print(元素.name, 元素.path,元素.is_dir())
j = 0
for 文件夹路径,子文件夹列表,文件列表 in os.walk(r'D:\multi_media\DOC\Study'):
    # print(文件夹路径)
    # print(子文件夹列表)
    # print(文件列表)
    for i in 文件列表:
        print(文件夹路径+i)
        j += 1
print(f'共发现{j}个文件')

