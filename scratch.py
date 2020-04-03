import requests
import pandas as pd
import math
# pd.set_option('expand_frame_repr', False)
# pd.set_option('display.max_rows', 100)

BASEURL = 'https://api.huobi.br.com'
# currencys = '/v1/common/currencys'
#
# currencys_url = BASEURL + currencys
# print(currencys_url)
# import requests
#
# resp = requests.get(currencys_url)
# print(resp)
# print(resp.status_code)
# print(resp.json())
# r_json = resp.json()
# data = r_json['data']
# #print(data)
# for d in data:
#     print(d)



# url = 'https://api.huobi.pro/market/history/kline?period=60min&size=100&symbol=fttusdt'
# resp = requests.get(url)
# #print(resp)
# #print(resp.json())
# resp_json = resp.json()
# print(resp_json['status'])
# data_list = resp_json['data']
# #for data in data_list:
#     #print(data)
#
# df = pd.DataFrame(data_list)
#
# print(df)
symbol = 'fttusdt'
hb_url = BASEURL + '/market/detail/merged' + '?' + 'symbol=' + symbol
hb_resp = requests.get(hb_url)

ticker = hb_resp.json()['tick']
#print(ticker)
huobi_ask = ticker['ask'][0]
huobi_bid = ticker['bid'][0]

print("huobi ask: " + str(huobi_ask))
print("huobi bid: " + str(huobi_bid))

ftx_url = 'https://ftx.com/api' + '/markets/FTT/USDT/orderbook?depth=1'
ftx_resp = requests.get(ftx_url)
ftx_ask = ftx_resp.json()['result']['asks'][0][0]
ftx_bid = ftx_resp.json()['result']['bids'][0][0]
print("ftx ask: " + str(ftx_ask))
print("ftx bid: " + str(ftx_bid))

if huobi_ask < ftx_bid:
    print("huobi discount")
elif huobi_bid > ftx_ask:
    print("huobi premium")
else:
    print("no spread")
