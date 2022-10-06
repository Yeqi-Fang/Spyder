import time
import re
import pandas as pd
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


class CrawlFromYoudao:
    path = r'../sourse/suorse.xlsx'
    url = r'https://fanyi.youdao.com/'
    wordlist = list(pd.read_excel(path, header=None)[0])

    def __init__(self, critical_time=3, wait_time=5,
                 webdriver_path=r"D:/迅雷下载/chromedriver_win32/chromedriver.exe",
                 print_word=True, browser_head=False):
        self.critical_time = critical_time
        self.wait_time = wait_time
        self.webdriver_path = webdriver_path
        self.print_word = print_word
        self.browser_head = browser_head

    @property
    def webdriver(self):
        if not self.browser_head:
            chrome_options = Options()
            chrome_options.add_argument('--headless')
            chrome_options.add_argument('--disable-gpu')
            wd = webdriver.Chrome(service=Service(self.webdriver_path),
                                  options=chrome_options)
        else:
            wd = webdriver.Chrome(service=Service(self.webdriver_path))
        wd.implicitly_wait(self.wait_time)
        # print(data)
        # 调用WebDriver 对象的get方法 可以让浏览器打开指定网址
        wd.get(self.url)
        return wd

    def get_content(self):
        wd = self.webdriver
        d = {}
        f1 = None
        for word in self.wordlist:
            time.sleep(random.uniform(1, 5))
            inp = wd.find_element(By.ID, "inputOriginal")
            inp.clear()
            inp.send_keys(word)
            # time.sleep(3)
            f2 = f = wd.find_elements(By.CSS_SELECTOR, 'div[class="dict__relative"]>span[class="no-link"]')
            n = 0
            while f1 == f2:
                f2 = f = wd.find_elements(By.CSS_SELECTOR, 'div[class="dict__relative"]>span[class="no-link"]')
                time.sleep(0.05)
                n += 0.05
                if n > self.critical_time:
                    print(f'{word} con not be found!')
                    break
            if n <= self.critical_time:
                f1 = f2
                L = []
                for i in f:
                    l = re.search(r'>(.)+<', i.get_attribute('outerHTML'))
                    j = l.group()
                    j = j.replace('&lt;', '<').replace('&gt;', '>')
                    L.append(j[1:-1])
                s = '\n'.join(L)
                d[word] = s
                if self.print_word:
                    print(word, s)
        if self.browser_head:
            wd.quit()
            # print(d)
        return d

    def into_excel(self, des=r'files/test.xlsx'):
        d = self.get_content()
        df = pd.DataFrame(d.values(), index=d.keys(), columns=['meanings'])
        df.to_excel(des)


if __name__ == '__main__':
    obj = CrawlFromYoudao(browser_head=True)
    obj.get_content()
