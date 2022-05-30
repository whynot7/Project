!pip install quandl
!pip install pandas_datareader

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import quandl


#import pandas_datareader
import datetime as datetime
from datetime import date
import pandas_datareader

import pandas_datareade

start = datetime.datetime(2017,1,1)
end = date.today()

BTC = web.DataReader('BTC-USD','yahoo', start,end)

BTC['MA50'] = BTC['Open'].rolling(50).mean()
BTC['MA200'] = BTC['Open'].rolling(200).mean()

BTC['MA50'].plot(label='MA50', figsize=(16,8), title='Moving Averages', color='orange')
BTC['MA200'].plot(label='MA200', color='green')
plt.legend()