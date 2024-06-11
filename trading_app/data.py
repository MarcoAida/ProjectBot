import requests
import pandas as pd
from config import BINANCE_API_KEY


def fetch_binance_data(symbol, interval, start_str):
    url = f'https://api.binance.com/api/v3/klines?symbol={symbol}&interval={interval}&startTime={start_str}'
    response = requests.get(url)
    data = response.json()
    df = pd.DataFrame(data,
                      columns=[
                          'timestamp', 'open', 'high', 'low', 'close',
                          'volume', 'close_time', 'quote_asset_volume',
                          'number_of_trades', 'taker_buy_base_asset_volume',
                          'taker_buy_quote_asset_volume', 'ignore'
                      ])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    df.set_index('timestamp', inplace=True)
    return df[['open', 'high', 'low', 'close', 'volume']]


if __name__ == "__main__":
    symbol = 'BTCUSDT'
    interval = '1d'
    start_str = '1609459200000'  # Example start time
    df = fetch_binance_data(symbol, interval, start_str)
    df.to_csv('btc_usdt.csv')  # Save data to a CSV file
    print(df.head())
