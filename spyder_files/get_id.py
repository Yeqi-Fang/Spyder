import requests
from lxml import etree


url = 'https://free.kuaidaili.com/free/inha/'
UA = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/81.0.4044.92 Safari/537.36 '
}

res = requests.get(url=url, headers=UA).text
l = etree.HTML(res)
td = l.xpath('//td[@data-title="IP"]/text()')
IPs = [f'\'http\': \'http://{i}\'' for i in td]
D = '{\n\t' + ',\n\t'.join(IPs) + '\n}'
print(D)
