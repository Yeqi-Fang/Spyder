import os
import re
import time
import numpy as np
import glob
import re
from fake_useragent import UserAgent
from youdao_word import CrawlFromYoudao

a = [1, 2, 3]
b = [4, 5, 6]
c = zip(a, b)
# print(dict(c))


a = re.compile(r'(\d+).f([1-5]+)')
b = "4131.f121247921"
f = re.search(a, b)
# print(f.group(2))
# d = f = 1
# import pandas as pd
# data = list(pd.read_excel('sourse/suorse.xlsx', header=None)[0])
# print(data)
t = time.time()


# print(t)
# tq = '女神的贴身高手 第31集 狠辣少主（更快收听搜索《绝世高手》付费版）'
# l = tq.split(' ')
# num = l[1]
# name = l[2].split('（')[0]
# print(num+' '+name)
# with open('../files/re.txt', 'r', encoding='utf-8') as f:
#     txt = f.read()
# print(txt)
# a = np.array([1, 2, 3, 4, 5, 6])

def find_max_page():
    os.chdir(r'C:\Users\FYQ\PycharmProjects\pythonProject1\files')
    a = re.compile(r'wordlist(\d+).xlsx')
    L = []
    for i in os.listdir():
        try:
            res = re.search(a, i)
            L.append(res.group(1))
        except:
            pass

        try:
            page = max(L)
        except:
            page = 1
    return page


if __name__ == '__main__':
    s = find_max_page()
    # print(s)
    # ua = UserAgent()
    # print(ua.random)
    # obj = CrawlFromYoudao(browser_head=True)
    # obj.content()
    # txt = '<td rowspan="1">大学化学实验（Ⅲ）(908005020_07)</td>'
    # b = re.compile(r'_(\d{2})')
    # print(re.search(b, txt).group(1))
    t = ((1, 2),)
    for i in t:
        print(i)
