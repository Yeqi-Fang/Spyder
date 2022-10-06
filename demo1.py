import time

import numpy as np
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import random
import cv2
webpath = r"D:/迅雷下载/chromedriver_win32/chromedriver.exe"
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
# wd = webdriver.Chrome(service=Service(webpath), options=chrome_options)
wd = webdriver.Chrome(service=Service(webpath))

# wd.implicitly_wait(self.wait_time)
for i in range(1, 1000):
    url = f'https://abook.hep.com.cn/ICourseFiles/5000002259/swfresourses/2021/4/2/1617327073560/1617327073560.files/{i}' \
          '.png '
    wd.get(url)
    wd.maximize_window()
    time.sleep(random.uniform(5, 10))
    # f1 = wd.get_screenshot_as_png()
    # with open(f'images/{i}.png', "wb") as f:
    #     f.write(f1)
    wd.save_screenshot(f'images/{i}.png')

    image = cv2.imread(f'images/{i}.png')
    num = int(np.count_nonzero(np.mean(image[0], axis=1) == 14) // 2)
    image = image[:, num:-num, :]
    cv2.imwrite(f'images/{i}.png', image)
