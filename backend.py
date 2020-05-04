import yfinance as yf

import pandas as pd

from datetime import datetime as dt

stockName = "SPY"
yfStockName = yf.Ticker(stockName)

data = yfStockName.history(period='max')

df = pd.DataFrame(data)

finalData = []
fromDate = '2019-02-03'
toDate = '2020-05-08'
recurringDeposit = 3800

fromDated = dt.strptime(fromDate, '%Y-%m-%d')

tempData = df[fromDate:toDate]
print(tempData)
total_investment = 0
total_worth = 0
total_stocks = 0
final = []
for index, data in tempData.iterrows():
    if (index.day == fromDated.day):
        highPrice = data['High']
        stocks = recurringDeposit / highPrice
        total_stocks += stocks
        total_worth = total_stocks * highPrice
        total_investment += recurringDeposit

        row = {
            'name': stockName,
            'date': index.strftime('%Y-%m-%d'),
            'high': highPrice,
            'stocks': stocks,
            'total_stocks': total_stocks,
            'total_investment': total_investment,
            'total_worth': total_worth
        }
        final.append(row)
        # print(final)
        print(index,  stockName, recurringDeposit, ' ', highPrice, '  ', stocks,
              '  ', total_stocks, '  ', total_worth, '  ', total_investment)
