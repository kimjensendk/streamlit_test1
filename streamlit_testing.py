import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf


st.write("""
# Simple Stock Price app
Shown are stock closing price and volume of google
""")

tickerSymbol = 'AAPL'

tickerData = yf.Ticker(tickerSymbol)


tickerDf = tickerData.history(period='1d', start = '2010-5-31', end='2023-1-31')

st.write("closing price")
st.line_chart(tickerDf.Close)

st.write("Volume")
st.line_chart(tickerDf.Volume)
