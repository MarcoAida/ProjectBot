import backtrader as bt


class SMACross(bt.SignalStrategy):

    def __init__(self):
        sma1, sma2 = bt.ind.SMA(period=50), bt.ind.SMA(period=200)
        crossover = bt.ind.CrossOver(sma1, sma2)
        self.signal_add(bt.SIGNAL_LONG, crossover)


def backtest(df):
    cerebro = bt.Cerebro()
    cerebro.addstrategy(SMACross)
    data = bt.feeds.PandasData(dataname=df)
    cerebro.adddata(data)
    cerebro.run()
    cerebro.plot()
