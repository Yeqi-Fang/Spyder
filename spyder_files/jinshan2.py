import json
import random
import time
import urllib.parse as parse
from hashlib import md5
import pandas as pd
import requests
from test import find_max_page
from fake_useragent import UserAgent

ua = UserAgent()
pro = {
    'http': 'http://122.9.101.6',
    'http': 'http://122.9.101.6',
    'http': 'http://112.14.47.6',
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
    'http': 'http://120.194.55.139'
}
wordlist = list(pd.read_excel('../sourse/suorse.xlsx', header=None)[0])


class CiBa:
    def generate_signature(self, params: dict) -> str:
        """
        生成signature
        """
        value_array = []
        keys = sorted(list(params.keys()))  # 对key进行排序
        for value in keys:
            value_array.append(str(params[value]))
        return md5(('/dictionary/word/query/web' + ''.join(value_array) + '7ece94d9f9c202b0d2ec557dg4r9bc').encode(
            'utf-8')).hexdigest()

    def get_meaning(self, word: str) -> str:
        UA = ua.random
        headers = {
            'Origin': 'https://www.iciba.com',
            'Referer': 'https://www.iciba.com/',
            'User-Agent': UA
        }
        params = {
            'client': 6,
            'key': 1000006,
            'timestamp': int(time.time() * 1000),
            'word': parse.quote(word)
        }
        params['signature'] = self.generate_signature(params)
        url = 'http://dict.iciba.com/dictionary/word/suggestion'
        # url = 'https://dict.iciba.com/dictionary/word/query/web?' + parse.urlencode(params)
        resp = requests.get(url, params=params, headers=headers)
        return resp.text


if __name__ == "__main__":
    # wordlist = ['bring about', 'get around', 'charge', 'pitch', 'scale']
    D = {}

    for word in wordlist:
        time.sleep(10 * random.random())
        d = json.loads(CiBa().get_meaning(word))
        try:
            meaning = d['message'][0]['paraphrase']
            D[word] = meaning
            print(f'{word}: {meaning}')
        # print(D)
        except:
            print(f'There is something wrong while looking up {word}')
            continue
    # for i in d['message']:
    #     print(i)

    df = pd.DataFrame(D.values(), index=D.keys(), columns=['meanings'])
    max_page = find_max_page()
    # df.to_excel(f'../files/wordlist{int(max_page) + 1}.xlsx')
    # print(D)
