import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
         # Simple Stock Price App
         
         Shown are the stock **closing price** and **volume** of Tesla
         """)

tickerSymbol = 'TSLA'

tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(period = '1d', start = '2023-05-01', end = '2023-08-01')

st.write("""
## Closing Price
""")

st.line_chart(tickerDf.Close)

st.write("""
## Closing Volume
""")

st.line_chart(tickerDf.Volume)