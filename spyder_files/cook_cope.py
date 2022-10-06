# txt = "buvid3=545CEB1B-53F2-8E49-595B-59E747EE35B647692infoc; _uuid=E108F423A-6510F-538C-5829-6A6FEEFC7F8950033infoc; buvid4=1CF13B26-8321-6D5D-F99F-0C0DD1F16AFE56885-022052317-ADgaJkpv35ZOxcM1+uv4wg%3D%3D; CURRENT_BLACKGAP=0; buvid_fp_plain=undefined; DedeUserID=390988907; DedeUserID__ckMd5=60cb9b6d4642ca7e; LIVE_BUVID=AUTO3516532987873040; blackside_state=0; rpdid=|(J|)RY~JmRk0J'uYlJkm)mlJ; b_ut=5; nostalgia_conf=-1; fingerprint=276ac81fc63a201cb586a2637471f247; buvid_fp=f6da40b8fba926f4c2a1b3e47be86e78; hit-dyn-v2=1; i-wanna-go-back=-1; CURRENT_QUALITY=80; SESSDATA=a8bafdc2%2C1678001944%2C9bc02%2A91; bili_jct=8e230b84c0d951f9508b48e306d2c996; sid=7665t9cr; PVID=2; b_nut=100; b_lsid=6102104C61_183129A5BDD; innersign=1; theme_style=light; bp_video_offset_390988907=702767026101289000; CURRENT_FNVAL=16"
# L = txt.split(';')
# D = {}
# for i in L:
#     D[i.split("=")[0]] = i.split("=")[1]
# print(D)
# print(lst)
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
    # print(li)
print(d)
