'''
1 > f12 > xhr > data check and search api data 

2 > check which request that browser made to api -> header is https://api.stock.naver.com/stock/ABNB.O/basic

distinguishable parameter

stockEndType	"stock"
reutersCode	"ABNB.O"
stockName	"에어비앤비 Class A"
stockNameEng	"Airbnb Inc Class A"
symbolCode	"ABNB"
tradeStopType	Object { code: "1", text: "운영.Trading", name: "TRADING" }
stockExchangeType	Object { code: "NSQ", zoneId: "EST5EDT", nationType: "USA", … }
stockExchangeName	"NASDAQ"
industryCodeType	Object { code: "572010", industryGroupKor: "소프트웨어 및 IT서비스", name: "INDUSTRY572010" }
delayTime	0
delayTimeName	"실시간"
compareToPreviousPrice	Object { code: "5", text: "하락", name: "FALLING" }
closePrice	"116.71"
compareToPreviousClosePrice	"-2.07"
fluctuationsRatio	"-1.74"



'''
from urllib import parse
from ast import literal_eval
import requests

ticker = 'intc'

page = requests.get("https://api.stock.naver.com/stock/%s.O/basic"%(ticker.upper()))
stockInfo = page.json()
print(stockInfo['stockNameEng'])
print(stockInfo['stockNameEng'])
print(stockInfo['currencyType']['name'])
print(stockInfo['stockItemTotalInfos'][1]['value'])
print(stockInfo['fluctuationsRatio'])


'''
urllib -> infos from url, html 

import urllib.request
response = urllib.request.urlopen('http://google.com') 
print(response.status) # respone status, online = 200

------------- using eval to evalute format

eval -> automatically converts variable into usable form , But take care about command injection error!
literal_eval -> ast.literal_eval is 


----------------requests

요청이 정상적으로 처리가 된 경우, 응답 전문(response body/payload)에 요청한 데이터가 담겨져 옵니다. 응답 전문은 크게 3가지 방식으로 읽어올 수 있습니다.

>>> requests.get("link").content
[binary original html text]
>>>requests.get("link").text
[utf-8 encoded texts]
>>>requests.get("link").json
[if data is formatted to json, write with dictionary]


https://www.daleseo.com/python-requests/

'''