import re
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from requests.exceptions import RequestException
import time


# 获取评论第一页的源码
def get_first_page_source(url, content_list):
    browser = webdriver.Chrome(service=Service(r"D:/迅雷下载/chromedriver_win32/chromedriver.exe"))
    browser.get(url)
    browser.execute_script('window.scrollBy(0,2000)')  # 调用js代码实现滑动
    time.sleep(4)  # 等待加载完毕
    content_list.append(browser.page_source)
    return browser.page_source


# 获取评论总页数
def get_max_size_page_info(html):
    pattern = re.compile('<div.*?header-page.*?result">共(\d+)页</span>', re.S)
    return re.findall(pattern, html)[0]


# 获取其他页的源码
def get_more_page_source(url, content_list):
    browser = webdriver.Chrome(service=Service(r"D:/迅雷下载/chromedriver_win32/chromedriver.exe"))
    # browser.set_window_size(1000,30000)
    browser.get(url)
    browser.execute_script('window.scrollBy(0,2000)')  # 调用js代码实现滑动
    time.sleep(4)  # 等待加载完毕
    content_list.append(browser.page_source)
    max_size = int(get_max_size_page_info(get_first_page_source(url, content_list)))
    for i in range(max_size - 1):
        next_btn = browser.find_element_by_css_selector('div.comment-header div.header-page a.next')  # 使用css选择器选择下一页a标签

        next_btn.click()
        time.sleep(1.5)
        content_list.append(browser.page_source)


# 获取评论信息
def get_comment(content):
    # 使用正则表达式匹配
    pattern = re.compile('<div.*?list-item.*?data-id="(\d+)".*?con.*?">.*?data-usercard-mid="(\d+)".*?name.*?">'
                         + '(.*?)</a>.*?<p.*?text">(.*?)</p>.*?</div>.*?</div>', re.S)
    for item in content:
        info = re.findall(pattern, item)
        for info_item in info:
            # 使用生成器规范化数据
            yield {
                'comment_id': info_item[0],
                'user_id': info_item[1],
                'user_name': info_item[2],
                'comment_text': info_item[3]
            }
    # return info


def main():
    url = 'https://www.bilibili.com/video/BV1Wh411d7hq?p=18&spm_id_from=pageDriver&vd_source=3aa269af84c7142b887fbe86bd30c8c3'
    comment_list = []
    get_more_page_source(url, comment_list)
    get_comment(comment_list)

    with open('D://comment_list.txt', 'a', encoding='utf-8') as f:
        for item in get_comment(comment_list):
            f.write(str(item) + '\n')
    print(len(comment_list))


if __name__ == '__main__':
    main()
