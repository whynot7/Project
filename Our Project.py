# Raw Package

# Data Source
import yfinance as yf

data = yf.download(tickers="BTC-USD", period="60d", interval="15m")

print(data)

#Data viz
import plotly.graph_objs as go

#declare figure
fig = go.figure()

#candlestick
fig.add_trace(go.Candlestick(x=data.index,
                             open=data["Open"],
                             high=data["High"],
                             low=data["Low"],
                             close=data["Close"], name = "market data"))

#Add titles
fig.update_layout(
    title="Bitcoin live share price evolution",
    yaxis_title="Stock Price (USD per Shares)")

#x-Axes
fig.update.xaxes(
    rangeslider_visible=True,
    rangeselector=dict(
        buttons=list([
            dict(count=15, label="15m",step="minute", stepmode="backward"),
            dict(count=45, label="45m", step="minute", stepmode="backward"),
            dict(count=1, label="htd",step="hour", stepmode="todate"),
            dict(count=6, label="15m",step="hour", stepmode="backward"),
            dict(step="all")
        ])
    )
)

#Show
fig.show()