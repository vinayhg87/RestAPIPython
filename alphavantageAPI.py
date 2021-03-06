#  https://www.quora.com/Stock-Market-Which-Python-libraries-can-I-use-to-access-stock-market-data-in-real-time
import requests as request
import time

count = 0

class alphaVantage(object):
    def apiCaller(self, stockName, timeInterval):
        response = ''
        global count
        if count < 5:
            try:
                response = request.get(
                    "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=NSE:" + stockName + "&interval=" + str(
                        timeInterval)
                    + "min&apikey=HFZZDTZ8XT126AW8")
                stockData = response.json()
                stockTime = list(stockData["Time Series (" + str(timeInterval) + "min)"])[1]
                print(stockData["Time Series (" + str(timeInterval) + "min)"][stockTime]["4. close"])
                count += 1
            except Exception as e:
                print("The response code is " + str(response.status_code))
                print(e)
        else:
            print("As per the alphaVantage policy, only 5 api calls are allowed in a minute."
                  + " This program will fetch the stock data after 60 seconds. Please wait !!!")
            time.sleep(60)
            count = 0
            self.apiCaller(stockName, timeInterval)


obj = alphaVantage()
obj.apiCaller('SBIN', 1)
obj.apiCaller('TATAMOTORS', 5)
obj.apiCaller('YESBANK', 5)
obj.apiCaller('GAIL', 1)
obj.apiCaller('IOC', 1)
obj.apiCaller('NTPC', 1)
obj.apiCaller('ICICIBANK', 1)
