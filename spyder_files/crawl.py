import requests
from lxml import etree
import pandas as pd
# url = 'https://www.bilibili.com/video/BV1Wh411d7hq?p=20&vd_source=3aa269af84c7142b887fbe86bd30c8c3'
# UA = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.27'}
# cook = {'buvid3': '545CEB1B-53F2-8E49-595B-59E747EE35B647692infoc', ' _uuid': 'E108F423A-6510F-538C-5829-6A6FEEFC7F8950033infoc', ' buvid4': '1CF13B26-8321-6D5D-F99F-0C0DD1F16AFE56885-022052317-ADgaJkpv35ZOxcM1+uv4wg%3D%3D', ' CURRENT_BLACKGAP': '0', ' buvid_fp_plain': 'undefined', ' DedeUserID': '390988907', ' DedeUserID__ckMd5': '60cb9b6d4642ca7e', ' LIVE_BUVID': 'AUTO3516532987873040', ' blackside_state': '0', ' rpdid': "|(J|)RY~JmRk0J'uYlJkm)mlJ", ' b_ut': '5', ' nostalgia_conf': '-1', ' fingerprint': '276ac81fc63a201cb586a2637471f247', ' buvid_fp': 'f6da40b8fba926f4c2a1b3e47be86e78', ' hit-dyn-v2': '1', ' i-wanna-go-back': '-1', ' CURRENT_QUALITY': '80', ' SESSDATA': 'a8bafdc2%2C1678001944%2C9bc02%2A91', ' bili_jct': '8e230b84c0d951f9508b48e306d2c996', ' sid': '7665t9cr', ' PVID': '2', ' b_nut': '100', ' b_lsid': '6102104C61_183129A5BDD', ' innersign': '1', ' theme_style': 'light', ' bp_video_offset_390988907': '702767026101289000', ' CURRENT_FNVAL': '16'}
# res = requests.get(url, headers=UA, cookies=cook).text
# print(res)
with open('../HTML_file/reer.html', 'r', encoding='utf-8') as f:
    txt = f.read()
# print(txt)
tree = etree.HTML(txt)
te = tree.xpath('//div[@class="user-name"]//text()')[:116]
te2 = tree.xpath('//div[@class="sub-user-name"]//text()')
txt1 = tree.xpath('//span[@class="reply-content root-reply"]')
txt2 = tree.xpath('//span[@class="reply-content sub-reply-content"]')

L = [''.join(i.xpath('.//text()')) for i in txt1]
L2 = [''.join(i.xpath('.//text()')) for i in txt2]
# print(len(L))
# print(len(te))
Se2 = pd.Series(L2, index=te2)
print(Se2)
Se2.to_excel('reer2.xlsx')
# print(te)
# print(len(te2))
# print(txt1)
# print(len(L2))
# test = txt1[0]
# print(test.xpath('.//text()'))