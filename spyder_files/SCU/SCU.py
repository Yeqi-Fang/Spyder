import time
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import selenium
import requests
from hashlib import md5
from PIL import Image

class Chaojiying_Client(object):

    def __init__(self, username, password, soft_id):
        self.username = username
        password = password.encode('utf8')
        self.password = md5(password).hexdigest()
        self.soft_id = soft_id
        self.base_params = {
            'user': self.username,
            'pass2': self.password,
            'softid': self.soft_id,
        }
        self.headers = {
            'Connection': 'Keep-Alive',
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)',
        }

    def PostPic(self, im, codetype):
        """
        im: 图片字节
        codetype: 题目类型 参考 http://www.chaojiying.com/price.html
        """
        params = {
            'codetype': codetype,
        }
        params.update(self.base_params)
        files = {'userfile': ('ccc.jpg', im)}
        r = requests.post('http://upload.chaojiying.net/Upload/Processing.php', data=params, files=files,
                          headers=self.headers)
        return r.json()

    def ReportError(self, im_id):
        """
        im_id:报错题目的图片ID
        """
        params = {
            'id': im_id,
        }
        params.update(self.base_params)
        r = requests.post('http://upload.chaojiying.net/Upload/ReportError.php', data=params, headers=self.headers)
        return r.json()


class SCU:

    def __init__(self, course: tuple, acceptable_nums: tuple,
                 url=r'http://zhjw.scu.edu.cn/login', wait_time=5,
                 webdriver_path=r"C:\Program Files\driver\chromedriver_win32\chromedriver.exe"):
        self.url = url
        self.wait_time = wait_time
        self.webdriver_path = webdriver_path
        self.course = course
        self.acceptable_nums = acceptable_nums

    def start_webdriver(self):
        wd = webdriver.Chrome(service=Service(self.webdriver_path))
        wd.implicitly_wait(self.wait_time)
        wd.get(self.url)
        wd.maximize_window()
        return wd

    def log_in(self):
        wd = self.start_webdriver()
        # 找到学号，密码
        wd.find_element(By.ID, 'input_username').send_keys('2021141220032')
        wd.find_element(By.ID, 'input_password').send_keys('Qwe027206')
        time.sleep(1.5)
        png = wd.get_screenshot_as_png()
        with open(r'D:\multi_media\DeskTop\test.png', 'wb') as f:
            f.write(png)
        # s = input('Please enter check code\n')
        s = self.recognize()
        wd.find_element(By.ID, 'input_checkcode').send_keys(s)
        wd.find_element(By.ID, 'loginButton').click()
        return wd

    @staticmethod
    def choose_course(wd, course, nums):
        b = re.compile(r'_(\d{2})')
        wd.find_element(By.CSS_SELECTOR, 'li[id="82020"]>a').click()

        # 点击选课
        wd.find_element(By.CSS_SELECTOR, 'li[id="1293220"]>a').click()
        wd.find_element(By.CSS_SELECTOR, 'li[id="1293218"]>a').click()
        # 如果非选课阶段下一段就会报错
        while True:
            try:
                wd.find_element(By.CSS_SELECTOR, 'li[id="zyxk"]>a').click()
                break
            except selenium.common.exceptions.NoSuchElementException:
                print("对不起，非选课阶段")
                wd.find_element(By.CSS_SELECTOR, 'li[id="1293220"]>a').click()
                # wd.find_element(By.CSS_SELECTOR, 'li[id="1293220"]>a').click()
        wd.switch_to.frame(wd.find_element(By.XPATH, '//*[@id="ifra"]'))
        wd.find_element(By.XPATH, '//*[@id="searchtj"]').send_keys(course)
        wd.find_element(By.XPATH, '//*[@id="queryButton"]').click()
        tr_list = wd.find_elements(By.CSS_SELECTOR, 'tbody[id="xirxkxkbody"]>tr')
        flag = 0
        for i in range(1, len(tr_list) + 1):
            input_ = wd.find_element(By.XPATH, f'//*[@id="xirxkxkbody"]/tr[{i}]')
            if 'disabled' not in input_.get_attribute('outerHTML'):
                try:
                    txt = wd.find_element(By.XPATH, f'//*[@id="xirxkxkbody"]/tr[{i}]/td[3]').get_attribute('outerHTML')
                    # if txt:
                    print(txt)
                    num_available = re.search(b, txt).group(1)
                    if str(num_available) in str(nums):
                        wd.find_element(By.XPATH, f'//*[@id="xirxkxkbody"]/tr[{i}]/td[1]/input').click()
                        flag = 1
                        break
                except selenium.common.exceptions.NoSuchElementException:
                    # print(E)
                    print(f"Cannot find that course:{course}. Probably beacause There's no Extracurricular capacity")

        if flag:
            wd.switch_to.default_content()
            wd.find_element(By.XPATH, '//*[@id="submitButton"]').click()
            time.sleep(5)
            return 1
        else:
            print('Failure!!!')
            return 0

    def manage(self, wd):
        # wd = self.log_in()
        for i in range(len(self.course)):
            stats = self.choose_course(wd, self.course[i], self.acceptable_nums[i])
            if stats:
                print(f'Congratulation! Course {self.course[i]} has been chosen successfully!!!')
            else:
                print(f'Course {self.course[i]} fails be chosen')

    @staticmethod
    def recognize():
        a = Image.open(r"D:\multi_media\DeskTop\test.png")
        a = a.crop((1270, 850, 1440, 925))
        a.save(r"D:\multi_media\DeskTop\test1.png")
        chaojiying = Chaojiying_Client('19382027996', 'qwe027206', '943168')  # 用户中心>>软件ID 生成一个替换 96001
        im = open(r"D:\multi_media\DeskTop\test1.png", 'rb').read()  # 本地图片文件路径 来替换 a.jpg 有时WIN系统须要//
        validation_code = chaojiying.PostPic(im, 1902)['pic_str']
        print(validation_code)  # 1902 验证码类型  官方网站>>价格体系 3.4+版 print 后要加()
        return validation_code


if __name__ == '__main__':
    scu = SCU(course=('908005020',), acceptable_nums=(('06', '08'),))
    wd = scu.log_in()
    scu.manage(wd)
