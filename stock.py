import pandas_datareader
import datetime as dt
import pandas as pd
import numpy as np
import gc

def data_fetch(stock, year, month, date):
    start = dt.datetime(year, month, date)
    end = dt.datetime.now()
    df = pandas_datareader.data.get_data_yahoo(stock, start, end)
    return df

stocks = ['2337', '1201', '1216', '1225', '1219', '1231', '1301', '1303', '1304', '1305', '1325', '1326', '1313',
        '1434', '1513', '1504', '1701', '1707', '1709', '1722', '1730', '2324', '2376', '2357', '2344', '2377', '2376', '2353']

for obj in stocks:
    try:
        f = data_fetch(obj + '.TWO', 2000, 1, 1)
    except:
        f = data_fetch(obj + '.TW', 2000, 1, 1)

    f.to_csv(obj + '.csv', encoding = 'Big5')
    del f
    gc.collect()
