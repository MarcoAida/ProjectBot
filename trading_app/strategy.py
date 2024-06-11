import numpy as np


def generate_signals(df):
    df['signal'] = 0
    df.loc[50:,
           'signal'] = np.where(df['SMA50'].iloc[50:] > df['SMA200'].iloc[50:],
                                1, -1)
    df['position'] = df['signal'].diff()
    return df
