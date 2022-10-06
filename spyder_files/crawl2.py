import requests
from bs4 import BeautifulSoup

# 对首页的页面数据进行爬取
url = 'http://www.shicimingju.com/book/xiyouji.html'
UA伪装 = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36'}
响应数据 = requests.get(url=url, headers=UA伪装)
响应数据.encoding = 'utf-8'
响应数据 = 响应数据.text
# 在首页中解析出章节的标题和详情页的url
# 1.实例化BeautifulSoup对象，需要将页面源码数据加载到该对象中
soup = BeautifulSoup(响应数据, 'lxml')
# 2.解析章节标题和详情页的url
li标签列表 = soup.select('.book-mulu > ul > li')
变量名 = open('../files/xiyouji.txt', 'w', encoding='utf-8')
# 要获取所有li标签中的a标签
for li in li标签列表:
    章节标题 = li.a.string
    详情页的url = r'http://www.shicimingju.com' + li.a['href']
    # 对详情页发起请求，解析出章节内容
    详情页数据 = requests.get(url=详情页的url, headers=UA伪装)
    详情页数据.encoding = 'utf-8'
    详情页数据 = 详情页数据.text
    # 解析出详情页中相关的章节内容
    详情页soup = BeautifulSoup(详情页数据, 'lxml')
    div标签 = 详情页soup.find('div', class_='chapter_content')
    # 将div标签中所有的文本内容获取
    章节内容 = div标签.text
    变量名.write(章节标题 + ':' + 章节内容 + '\n')
    print(章节标题, '爬取成功！！！')
