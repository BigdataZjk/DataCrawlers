import configparser
import json

import requests
import urllib3

# 配置文件声明
cfg = configparser.ConfigParser()
cfg.read(r'D:\GitProjects\DataCrawlers\resources\setting.ini')
uali = cfg.get('http', 'ua').split('----')
url = cfg.get('http', 'ad_url')
headdic = {}
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
headdic[
    'User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.35'
headdic['X-Requested-With'] = 'XMLHttpRequest'
headdic['X-XSRF-TOKEN'] = 'CbreHc2DB7PyWmXQmNQYFcYeWMSxHWRd'

form = {'type': 'contact', 'contact': '123456', 'captcha': '', 'query_password': '', 'order_no': ''}
# 忽略警告
urllib3.disable_warnings()
try:
    # POST请求
    req = requests.post(url, headers=headdic, data=form, verify=False)
    resp = req.text.encode().decode('unicode_escape')
    # print(r.text.encode().decode('unicode_escape'))
    '''
    {
        "message": "success",
        "data": {
            "list": [
                {
                    "id": 10887,
                    "created_at": "2022-11-05 11:27:16",
                    "order_no": "2022110511271652hhG",
                    "contact": "123456",
                    "status": 2,
                    "send_status": 0,
                    "count": 1,
                    "paid": 1650,
                    "product_name": "NRK(CNC)--充值卡",
                    "contact_ext": "{}"
                }
            ],
            "msg": ""
        }
    }
    '''
    if resp:
        respJson = json.loads(resp)
        print(respJson)
        respJson['data']
except Exception as e:
    print('异常抛出:\r\n%s\r\n异常数据%s'%(e,resp))
finally:print('done!')




