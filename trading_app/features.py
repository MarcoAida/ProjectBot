import pandas as pd


def compute_rsi(series, period=14):
    delta = series.diff(1)
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)
    avg_gain = gain.rolling(window=period).mean()
    avg_loss = loss.rolling(window=period).mean()
    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    return rsi


def compute_macd(series, fast=12, slow=26, signal=9):
    fast_ema = series.ewm(span=fast, min_periods=slow).mean()
    slow_ema = series.ewm(span=slow, min_periods=slow).mean()
    macd = fast_ema - slow_ema
    signal_line = macd.ewm(span=signal, min_periods=signal).mean()
    macd_hist = macd - signal_line
    return macd, signal_line, macd_hist


def compute_bollinger_bands(series, period=20, std_dev=2):
    sma = series.rolling(window=period).mean()
    std = series.rolling(window=period).std()
    upper_band = sma + (std_dev * std)
    lower_band = sma - (std_dev * std)
    return upper_band, lower_band


def compute_features(df):
    df['SMA50'] = df['close'].rolling(window=50).mean()
    df['SMA200'] = df['close'].rolling(window=200).mean()
    df['RSI'] = compute_rsi(df['close'])
    df['MACD'], df['MACD_signal'], df['MACD_hist'] = compute_macd(df['close'])
    df['upper_band'], df['lower_band'] = compute_bollinger_bands(df['close'])
    return df
