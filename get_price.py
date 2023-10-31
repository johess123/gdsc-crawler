import requests
import datetime
import time

stock = ["1101","2330","2388"]
date = datetime.datetime.today().strftime("%Y%m%d")
print("現在時間",datetime.datetime.now())
for i in range(len(stock)):
    # 爬股價
    url = "https://www.twse.com.tw/rwd/zh/afterTrading/STOCK_DAY_AVG?date="+date+"&stockNo="+stock[i]+"&response=json&_=1697638279385"
    r = requests.get(url)
    result = r.json()
    # bot token
    token = "6718510325:AAF1by3LnmV2nPit9NBtxKdExhUK1MEOISY"
    # 使用者 id
    chat_id="5740033148"
    # 訊息
    message = "股票 "+str(stock[i])+" 今日的收盤價為 "+result["data"][-2][1]
    # bot 送訊息
    url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"
    requests.get(url)
    # 每次都停 3 秒
    time.sleep(3)
