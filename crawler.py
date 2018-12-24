#coding=utf-8
#python爬虫使用代理ip
#免费代理ip池: http://www.freeyuming.cn/ip

import requests
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                        'AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/64.0.3282.186 Safari/537.36'}
url = 'https://www.baidu.com/'
proxy="http://183.47.40.35:8088"  #这是免费ip
r = requests.get(url, headers=header, proxies={"http":proxy},timeout=5)
print(r.text)
