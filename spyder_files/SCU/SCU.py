import time
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import selenium


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
        s = input('Please enter check code\n')
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
                    #     print(txt)
                except selenium.common.exceptions.NoSuchElementException:
                    # print(E)
                    print(f"Cannot find that course:{course}. Probably beacause There's no Extracurricular capacity")
                num_available = re.search(b, txt).group(1)
                if str(num_available) in str(nums):
                    wd.find_element(By.XPATH, f'//*[@id="xirxkxkbody"]/tr[{i}]/td[1]/input').click()
                    flag = 1
                    break
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


if __name__ == '__main__':
    scu = SCU(course=('908005020',), acceptable_nums=(('06', '08'),))
    wd = scu.log_in()
    scu.manage(wd)
