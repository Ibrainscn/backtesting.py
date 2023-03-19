from backtesting import Backtest, Strategy
from backtesting.lib import crossover

from backtesting.test import SMA, GOOG


class SmaCross(Strategy):
    def init(self):
        price = self.data.Close
        self.ma1 = self.I(SMA, price, 10, name="SMA_10",overlay=True)
        self.ma2 = self.I(SMA, price, 20, name="SMA_20",overlay=True)

    def next(self):
        if crossover(self.ma1, self.ma2):
            # self.position.close()
            self.buy()
        elif crossover(self.ma2, self.ma1):
            # self.position.close()
            self.sell()


bt = Backtest(GOOG, SmaCross, commission=.002,
              exclusive_orders=True)
stats = bt.run()
bt.plot()
print(stats)
