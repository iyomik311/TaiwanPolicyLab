import random

from game import TaiwanGame


class TaiwanSimulator:

    def __init__(self, us_support, china_pressure, taiwan_position):
        self.game = TaiwanGame(
            us_support,
            china_pressure,
            taiwan_position
        )

    def run(self, rounds=100):

        us_matrix, china_matrix = self.game.payoff_matrix()

        us_total = 0
        china_total = 0

        history = []

        for _ in range(rounds):

            us_choice = random.randint(0, 1)
            china_choice = random.randint(0, 1)

            us_score = us_matrix[us_choice][china_choice]
            china_score = china_matrix[us_choice][china_choice]

            us_total += us_score
            china_total += china_score

            history.append({
                "US Strategy": us_choice,
                "China Strategy": china_choice,
                "US Payoff": us_score,
                "China Payoff": china_score
            })

        return {
            "US Total": us_total,
            "China Total": china_total,
            "US Average": us_total / rounds,
            "China Average": china_total / rounds,
            "History": history
        }
