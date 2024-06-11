#pip install -r requirements.txt

#python app.py

from data import fetch_binance_data
from features import compute_features
from strategy import generate_signals
from backtest import backtest
from flask import Flask
from visualizeDash import create_dash_app  # or create_streamlit_app

# Fetch data
symbol = 'BTCUSDT'
interval = '1d'
start_str = '1609459200000'
df = fetch_binance_data(symbol, interval, start_str)

# Compute features
df = compute_features(df)

# Generate signals
df = generate_signals(df)

# Backtest strategy
backtest(df)

# Initialize Flask server
server = Flask(__name__)

# Run visualization app
dash_app = create_dash_app(server, df)  # or create_streamlit_app(df)

if __name__ == '__main__':
    server.run(debug=True)
