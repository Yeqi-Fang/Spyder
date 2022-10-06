import time
import requests
from fake_useragent import UserAgent
from lxml import etree
import random
from pathlib import Path
import zipfile
import os


class PPT:
    url0 = 'https://www.1ppt.com/moban/'
    ua = UserAgent()

    def __init__(self, name='dangzheng', max_sleep_time=10,
                 min_sleep_time=5, path='files/zipfile'):
        self.name = name
        self.max_sleep_time = max_sleep_time
        self.min_sleep_time = min_sleep_time
        self.path = path

    @property
    def max_page(self):
        url0 = self.url0 + self.name + '/'
        UA = {'User-Agent': self.ua.random}
        res = requests.get(url0, headers=UA)
        res.encoding = 'gbk'
        res = res.text
        tree = etree.HTML(res)
        pages = tree.xpath('/html/body/div[5]/dl/dd/div[2]/ul/li/a/text()')
        max_page = pages[-3]
        return int(max_page)

    @staticmethod
    def clear():
        for i in os.listdir():
            if not (i.endswith('.pptx') or i.endswith('.ppt')):
                try:
                    os.remove(i)
                except PermissionError as e:
                    print(e)

    @staticmethod
    def zip(path):
        os.chdir(os.path.split(path)[0])
        with zipfile.ZipFile(os.path.split(path)[1], 'r') as f:
            for file_name in f.namelist():
                des = Path(f.extract(file_name))
                try:
                    des.rename(file_name.encode('cp437').decode('gbk'))
                except FileExistsError as e:
                    print('FileExistsError:', e)
                    name = file_name.encode('cp437').decode('gbk').split('.')[0] + '(1)' + '.' + \
                           file_name.encode('cp437').decode('gbk').split('.')[-1]
                    des.rename(name)
                    # des.rename(file_name.encode('cp437').decode('gbk') + '(1)')

    def get_ppt(self):
        max_page = self.max_page
        # print(type(max_page))
        for i in range(1, max_page):
            UA = {'User-Agent': self.ua.random}
            url = f'https://www.1ppt.com/moban/{self.name}/ppt_{self.name}_{i}.html'
            res = requests.get(url, headers=UA)
            res.encoding = 'gbk'
            res = res.text
            tree = etree.HTML(res)
            a_list = tree.xpath('/html/body/div[5]/dl/dd/ul/li/h2/a/@href')
            urls = ['https://www.1ppt.com' + i for i in a_list]

            for url in urls:
                UA = {'User-Agent': self.ua.random}
                res1 = requests.get(url, headers=UA)
                res1.encoding = 'gbk'
                res1 = res1.text
                tree = etree.HTML(res1)
                url_next = tree.xpath('/html/body/div[4]/div[1]/dl/dd/ul[1]/li/a/@href')[0]
                name = tree.xpath('/html/body/div[4]/div[1]/dl/dd/div[1]/h1/text()')[0][:-7]
                url_next = 'https://www.1ppt.com' + url_next
                res2 = requests.get(url_next, headers=UA)
                res2.encoding = 'gbk'
                res2 = res2.text
                tree = etree.HTML(res2)
                url_fin = tree.xpath('/html/body/dl/dd/ul[2]/li[1]/a/@href')[0]
                zip_file = requests.get(url_fin, headers=UA).content
                os.chdir(r'C:\Users\FYQ\PycharmProjects\pythonProject1')
                with open(f'{self.path}\\{name}.zip', 'wb') as f:
                    f.write(zip_file)
                print(f'Successfully download {name}')
                time.sleep(random.uniform(self.min_sleep_time, self.max_sleep_time))
                self.zip(f'{self.path}\\{name}.zip')
                self.clear()
                print(f'Successfully decompress {name}')


if __name__ == '__main__':
    ppt = PPT(path=r'D:\DownLoads\新建文件夹', name='jianjie',
              max_sleep_time=20, min_sleep_time=10)
    ppt.get_ppt()
