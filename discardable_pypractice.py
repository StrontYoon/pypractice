'''

from urllib import parse
from ast import literal_eval
import requests

def get_sise(code, start_time, end_time, time_from='day') :
    get_param = {
    	'symbol':code,
	    'requestType':1,
	    'startTime':start_time,
	    'endTime':end_time,
	    'timeframe':time_from
    }
    get_param = parse.urlencode(get_param)
    url="https://api.finance.naver.com/siseJson.naver?%s"%(get_param)
    response = requests.get(url)
    print(literal_eval(response.text.strip()))
    return literal_eval(response.text.strip())
    
get_sise('005930', '20210919', '20210920', 'day')

'''
import requests

page = requests.get("https://api.stock.naver.com/stock/INTC.O/basic")
info = page.json()
print(page)
print(info)

num = 1
print(f"{num=}")
