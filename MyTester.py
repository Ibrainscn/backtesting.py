from backtesting import Backtest, Strategy
from backtesting.lib import crossover

from backtesting.test import SMA
import pandas as pd
import numpy as np


def ma_diff(ma1, ma2):
    res = np.zeros(ma1.shape)
    res[ma1 > ma2] = 1
    res[ma1 < ma2] = -1
    return res

def bar_mean(open, high, low, close):
    return (open + high + low + close) / 4

class SmaCross(Strategy):
    ma_fast = 28
    ma_slow = 49
    n = 0
    def init(self):
        price = (self.data.Open + self.data.High + self.data.Low + self.data.Close) / 4
        self.ma1 = self.I(SMA, price, self.ma_fast, name="sma_fast", overlay=True)
        self.ma2 = self.I(SMA, price, self.ma_slow, name="sma_slow", overlay=True)
        self.ma1_2 = self.I(ma_diff, self.ma1, self.ma2, name="ma1-2", overlay=False)
        self.bar_mean = self.I(bar_mean, self.data.Open, self.data.High, self.data.Low, self.data.Close, name="bar_mean", overlay=True)
        print(f"self.bar_mean: \n {self.bar_mean}")
        print(f"self.bar_mean: \n {len(self.bar_mean)}")


    def next(self):
        if crossover(self.ma1, self.ma2):
            # if not self.position:
            self.position.close()
            self.buy(size=1)
        elif crossover(self.ma2, self.ma1):
            self.position.close()
            #self.sell(size=1)

        self.n += 1
        if self.n < 5:
            print(f"n = {self.n} self.data: \n {self.data.Close[-1]}")



NQ = pd.read_csv('backtesting/test/NQ.csv')
bt = Backtest(NQ, SmaCross, cash=100000, commission=.002,
              exclusive_orders=True, hedging=True)

stats = bt.run()
"""
stats = bt.optimize(
    ma_fast = range(3, 50, 1),
    ma_slow = range(5, 50, 1),
    maximize = "Return [%]",
    constraint = lambda param: param.ma_fast < param.ma_slow
    )
"""
bt.plot()
print(stats)
