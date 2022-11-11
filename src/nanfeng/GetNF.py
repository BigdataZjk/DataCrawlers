import datetime
import json
import random
from multiprocessing.pool import Pool

import requests

# 当前时间 用于计算卡密时间
nowTime = datetime.datetime.now()

user_agent = [
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
    "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
]
# 目标
url = 'http://lol.021tc.pw/ajax.php?act=query'
url_detail = 'http://lol.021tc.pw/ajax.php?act=order'
# 数据表单
d = {'type': '0', 'qq': 'xx', 'page': '1'}
# 请求头
req_header = dict()
req_header['Accept'] = 'application/json, text/javascript, */*; q=0.01'
req_header['Accept-Encoding'] = 'gzip, deflate'
req_header['Cache-Control'] = 'no-cache'
req_header['Content-Type'] = 'application/x-www-form-urlencoded; charset=UTF-8'
req_header[
    'Cookie'] = 'PHPSESSID=q8takeqmgj3iibick3ejhmmqu7; sec_defend=1fedbb2a10967706febb5f4a3bc21a7fd1b56dc0618f3b5da2bc7431d30ae109; mysid=e4329b0ab406cf174b330665eebac3e3; op=false; counter=1'
req_header['Pragma'] = 'no-cache'
req_header[
    'User-Agent'] = random.choice(user_agent)
req_header['X-Requested-With'] = 'XMLHttpRequest'
req_header['Referer'] = 'http://lol.021tc.pw/'
req_header['Origin'] = 'http://lol.021tc.pw'


# 单人数据爬取
def goSingle(form):
    req_header['User-Agent'] = random.choice(user_agent)
    # POST请求
    r = requests.post(url, headers=req_header, data=form, verify=False)

    reqStr = r.text
    reqJson = json.loads(reqStr)
    dataJson = json.loads(json.dumps(reqJson['data']))
    if dataJson:
        for i in dataJson:
            buyTime = datetime.datetime.strptime(i['addtime'], "%Y-%m-%d %H:%M:%S")
            expTime = (nowTime - buyTime).total_seconds() / 3600
            # 如果有则请求明细 并打印
            if expTime <= 24:
                dt = {'id': i['id'], 'skey': i['skey']}
                req_header['User-Agent'] = random.choice(user_agent)
                rt = requests.post(url_detail, headers=req_header, data=dt, verify=False)
                rtJson = json.loads(rt.text)
                with open(r'D:\GitProjects\DataCrawlers\resources\Card.txt', mode='a') as res:
                    print(("辅助：%s 时间：%s 消费：%s 卡密：%s 查询：%s 备注：%s\r" % (
                        rtJson['name'], rtJson['date'], rtJson['money'], rtJson['kminfo'], rtJson['inputs'],
                        rtJson['desc'])))
                    res.write("辅助：%s 时间：%s 消费：%s 卡密：%s 查询：%s 备注：%s\r" % (
                        rtJson['name'], rtJson['date'], rtJson['money'], rtJson['kminfo'], rtJson['inputs'],
                        rtJson['desc']))
            else:
                print("有记录qq但不小于两天:%s " % (form['qq']))
    else:
        print("无记录qq：%s" % (form['qq']))


if __name__ == '__main__':
    qqli = []
    with open(r'D:\GitProjects\DataCrawlers\resources\Card.txt', mode='w') as res:
        res.truncate()
        res.close()
    with open(r'D:\GitProjects\DataCrawlers\resources\SearchInfo.txt', mode='r') as qf:
        for qq in qf:
            d['qq'] = qq.strip()
            qqli.append(d)
            d = {'type': '0', 'qq': 'xx', 'page': '1'}
    qf.close()
    pool = Pool(processes=4)
    result = pool.map(goSingle, qqli)
    pool.close()
    pool.join()
