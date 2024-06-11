#Using Streamlit:

import streamlit as st
import plotly.graph_objects as go

st.title('Cryptocurrency Trading Dashboard')

fig = go.Figure(data=[
    go.Candlestick(x=df.index,
                   open=df['open'],
                   high=df['high'],
                   low=df['low'],
                   close=df['close'])
])

fig.update_layout(title='Price Chart')
st.plotly_chart(fig)

st.line_chart(df[['SMA50', 'SMA200']])
