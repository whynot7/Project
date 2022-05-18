!pip install yfinance
!pip install plotly
!pip install pandas
!pip install numpy

# Raw Package
import numpy as np
import pandas as pd

# Data Source
import yfinance as yf

data = yf.download("SNP")

#Data viz
import plotly.graph_objs as go

#declare figure
fig = go.Figure()

#candlestick
fig.add_trace(go.Candlestick(x=data.index,
                             open=data["Open"],
                             high=data["High"],
                             low=data["Low"],
                             close=data["Close"], name = "market data"))

#Add titles
fig.update_layout(
    title="S&P 500 live share price evolution",
    yaxis_title="S&P 500 Price (USD per Shares)")

#x-Axes
fig.update_xaxes(
    rangeslider_visible=True,
    rangeselector=dict(
        buttons=list([
            dict(count=1, label="1D",step="day", stepmode="backward"),
            dict(count=5, label="5D", step="day", stepmode="backward"),
            dict(count=1, label="1M",step="month", stepmode="backward"),
            dict(count=6, label="6M",step="month", stepmode="backward"),
            dict(count=1, label="YTD",step="year", stepmode="todate"),
            dict(count=1, label="1Y",step="year", stepmode="backward"),
            dict(count=5, label="5Y",step="year", stepmode="backward"),
            dict(step="all")
        ])
    )
)

#Show
fig.show()