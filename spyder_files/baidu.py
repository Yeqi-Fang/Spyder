import requests
from lxml import etree
import json

url = 'https://fanyi.baidu.com/sug'
UA = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 '
                  'Safari/537.36 Edg/105.0.1343.27'}

txt = '''Accept: application/json, text/javascript, */*; q=0.01
    Accept-Encoding: gzip, deflate, br
    Accept-Language: zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7
    Connection: keep-alive
    Content-Length: 6
    Content-Type: application/x-www-form-urlencoded; charset=UTF-8
    Cookie: BIDUPSID=7FE508AF90F81318F47AA3499C156ACA; PSTM=1653298313; BAIDUID=7FE508AF90F8131885CDBDDDBC0E6E2A:FG=1; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; APPGUIDE_10_0_2=1; BDUSS=JvdUQtfkVmMWpXZ0c3TWl5RUMya09IaWZoSnhTREt6RUFldU05anBrLWdhUkZqRVFBQUFBJCQAAAAAAAAAAAEAAACDs7Wmy8nK83F3ZWFzZHgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKDc6WKg3OliZ0; BDUSS_BFESS=JvdUQtfkVmMWpXZ0c3TWl5RUMya09IaWZoSnhTREt6RUFldU05anBrLWdhUkZqRVFBQUFBJCQAAAAAAAAAAAEAAACDs7Wmy8nK83F3ZWFzZHgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKDc6WKg3OliZ0; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; BA_HECTOR=8h8g24ak24ah208l2lake13p1hhgec116; ZFY=Eqfgj9HouuG0hSPu3mEGCErNv21LYOV5QSxs2QTpRi0:C; BAIDUID_BFESS=7FE508AF90F8131885CDBDDDBC0E6E2A:FG=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1662179339,1662359343,1662424356,1662541649; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1662541649; ab_sr=1.0.1_MTBiOTliYmQwMTU5MjYwMDZjNzQ4YTljN2U2ZDY4NmI5NWFhNzc0MDlmMjg1OTU0YzZhOTg4Y2MwNjA2ZmUzZWU2NjZiODFjNTU3MTM5N2ExNTFhYWY2NWEwMDUzM2M2NDg3NzNmMGNkYmI4YjBlNDE0MmE1NjNlNjc5MTY0MDAwNTFhYTUwMjM5M2YzMDczOWFkMWEzMGY5ZDM4OTVjM2VjNTczM2IxNjAyMzI5NzBhMGNmZjRjNWRjNzQyNzIz
    Host: fanyi.baidu.com
    Origin: https://fanyi.baidu.com
    Referer: https://fanyi.baidu.com/?aldtype=16047
    sec-ch-ua: "Microsoft Edge";v="105", " Not;A Brand";v="99", "Chromium";v="105"
    sec-ch-ua-mobile: ?0
    sec-ch-ua-platform: "Windows"
    Sec-Fetch-Dest: empty
    Sec-Fetch-Mode: cors
    Sec-Fetch-Site: same-origin
    User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.27
    X-Requested-With: XMLHttpRequest'''
l = txt.split('\n')
d = {}
for i in l:
    li = i.split(':')
    d[li[0]] = li[1]
d['kw'] = 'charge'
res = requests.post(url, headers=UA, data=d)
# res.encoding = 'utf-8'
txt = res.text
# print(txt)
d = json.loads(txt)
for i in d['data']:
    print(i)
