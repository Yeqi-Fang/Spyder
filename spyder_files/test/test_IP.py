import requests
from fake_useragent import UserAgent

ua = UserAgent()
proxies = {
    'http': 'http://120.220.220.95',
    'http': 'http://112.14.47.6',
    'http': 'http://183.247.199.215',
    'http': 'http://223.96.90.216',
    'http': 'http://120.220.220.95',
    'http': 'http://120.220.220.95',
    'http': 'http://120.220.220.95',
    'http': 'http://120.220.220.95',
    'http': 'http://61.216.185.88',
    'http': 'http://223.96.90.216',
    'http': 'http://47.106.105.236',
    'http': 'http://61.216.185.88',
    'http': 'http://61.216.156.222',
    'http': 'http://223.96.90.216',
    'http': 'http://122.9.101.6'
}

head = {
    'user-agent': ua.random
}
print(requests.get('http://httpbin.org/ip', timeout=3, proxies=proxies).text)
