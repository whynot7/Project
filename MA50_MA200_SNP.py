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


start = datetime.datetime(2017,1,1)
end = date.today()

SNP = web.DataReader('SNP','yahoo', start,end)

SNP['MA50'] = SNP['Open'].rolling(50).mean()
SNP['MA200'] = SNP['Open'].rolling(200).mean()

SNP['MA50'].plot(label='MA50', figsize=(16,8), title='Moving Averages', color='orange')
SNP['MA200'].plot(label='MA200', color='green')
plt.legend()