import datetime
import json
import random
from multiprocessing.pool import Pool
import requests

import configparser

# 配置文件声明
cfg = configparser.ConfigParser()
cfg.read(r'D:\GitProjects\DataCrawlers\resources\setting.ini')
ua = cfg.get('http', 'ua')
url = cfg.get('http', 'ad_url')

headdic= {}
headdic['Accept'] = 'application/json, text/plain, */*'
headdic['Accept-Encoding'] = 'gzip, deflate'
headdic['Accept-Language'] = 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6'
headdic['Connection'] = 'keep-alive'
headdic['Content-Length'] = '62'
headdic['Content-Type'] = 'application/x-www-form-urlencoded'
headdic['Cookie'] = 'customer=e6d3a6f9a721cae5d7b86e8a379a5007'
headdic['Host'] = 'adfk4.top'
headdic['Origin'] = 'http://adfk4.top'
headdic['Referer'] = 'http://adfk4.top/p/n63gxdmmi2b139r0wvap'
headdic['User-Agent'] = random.choice(list(ua))
headdic['X-Requested-With'] = 'XMLHttpRequest'
headdic['X-XSRF-TOKEN'] = 'seYPGFr2WN8DKTSacJDrYfwr5kzMreXw'

# POST请求
r = requests.get(url, headers=headdic,verify=False)
print(r.text)
