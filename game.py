import numpy as np


class TaiwanGame:
    def __init__(self, us_support, china_pressure, taiwan_position):
        self.us_support = us_support
        self.china_pressure = china_pressure
        self.taiwan_position = taiwan_position

    def payoff_matrix(self):
        us = self.us_support
        cn = self.china_pressure
        tw = self.taiwan_position

        us_payoff = np.array([
            [5 + us - cn, 3 + us - tw],
            [2 - cn, 1 - tw]
        ])

        china_payoff = np.array([
            [5 + cn - us, 2 + cn],
            [3, 1 + tw]
        ])

        return us_payoff, china_payoff
