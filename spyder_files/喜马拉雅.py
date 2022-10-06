import os.path
import time
import random
import requests
import json

url = 'https://www.ximalaya.com/revision/album/v1/getTracksList?albumId=16411402&pageNum=1&sort=0'
UA = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/81.0.4044.92 Safari/537.36 '
}

proxies = {
    'http': 'http://202.109.157.64',
    'http': 'http://120.194.55.139',
    'http': 'http://39.108.101.55',
    'http': 'http://61.216.156.222',
    'http': 'http://120.194.55.139',
    'http': 'http://101.200.127.149',
    'http': 'http://183.247.211.156',
    'http': 'http://101.200.127.149',
    'http': 'http://101.200.127.149',
    'http': 'http://120.220.220.95',
    'http': 'http://47.113.90.161',
    'http': 'http://120.194.55.139',
    'http': 'http://47.106.105.236',
    'http': 'http://120.194.55.139',
    'http': 'http://27.42.168.46'
}

for page in range(1, 67):
    url = f'https://www.ximalaya.com/revision/album/v1/getTracksList?albumId=16411402&pageNum={page}&sort=0'
    res = requests.get(url=url, headers=UA, proxies=proxies).text
    # with open('re.txt', 'w', encoding='utf-8') as f:
    #     f.write(res)
    l = json.loads(res)
    # print(l)
    for i in l['data']['tracks']:
        title = i['title']
        l = title.split(' ')
        # print(title)
        num = l[1]
        try:
            name = l[2]
        except:
            name = ''
        title = num + ' ' + name
        file_name = f'../audio/{title}.m4a'
        if os.path.exists(file_name):
            continue
        id = i['trackId']
        # print(id)
        urli = f'https://www.ximalaya.com/revision/play/v1/audio?id={id}&ptype=1'
        resi = requests.get(urli, headers=UA, proxies=proxies).text
        d = json.loads(resi)
        time.sleep(random.random())
        url_ii = d['data']['src']
        # print(url_ii)
        audio = requests.get(url_ii).content
        # print(audio)
        with open(file_name, 'wb') as f:
            f.write(audio)
            print(f'{title}  下载成功！！！')
    time.sleep(3 * random.random())
