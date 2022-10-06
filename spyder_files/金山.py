import requests
from lxml import etree
import json
import time
url = 'http://dict.iciba.com/dictionary/word/suggestion?word=fun&nums=5&ck=709a0db45332167b0e2ce1868b84773e&timestamp' \
      '=1662543850553&client=6&uid=123123&key=1000006&is_need_mean=1&signature=5d8d4dc7672b18568f648290d7966a89 '
UA = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 '
                  'Safari/537.36 Edg/105.0.1343.27'}

txt = '''word: fun
nums: 5
ck: 709a0db45332167b0e2ce1868b84773e
client: 6
uid: 123123
key: 1000006
is_need_mean: 1
signature: 5d8d4dc7672b18568f648290d7966a89'''
l = txt.split('\n')
d = {}
for i in l:
    li = i.split(':')
    d[li[0]] = li[1]
d['timestamp'] = time.time()
# d['kw'] = 'charge'
res = requests.get(url, headers=UA, params=d)
# res.encoding = 'utf-8'
txt = res.text
print(txt)
# d = json.loads(txt)
# for i in d['data']:
#     print(i)
