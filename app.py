import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
    # Simple Stock Price 
""")

tickerSymbol = st.text_input("Which Stocks you want: ")
st.write('Stock Price of ', tickerSymbol)

tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2021-1-8')

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)
