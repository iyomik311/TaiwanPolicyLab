import random

from game import TaiwanGame
from risk import calculate_risk
from economy import calculate_economic_cost
from silicon import silicon_shield_score
from analysis import generate_analysis
from nash import calculate_nash, format_equilibria


class TaiwanSimulator:
    """
    Taiwan Strait Policy Lab Simulation Engine (Version 2)

    입력된 정책 변수들을 기반으로
    게임이론, 군사위험, 경제비용,
    Silicon Shield를 종합 분석한다.
    """

    def __init__(
        self,
        us_support,
        china_pressure,
        taiwan_position,
        semiconductor,
        interdependence,
        sanctions,
    ):

        self.us_support = us_support
        self.china_pressure = china_pressure
        self.taiwan_position = taiwan_position
        self.semiconductor = semiconductor
        self.interdependence = interdependence
        self.sanctions = sanctions

        self.game = TaiwanGame(
            us_support,
            china_pressure,
            taiwan_position
        )

    def _choose_strategy(self):
        """
        정책 변수에 따른 간단한 전략 선택
        """

        # 미국 전략
        if self.us_support >= 7:
            us_strategy = 1
        else:
            us_strategy = 0

        # 중국 전략
        pressure_score = (
            self.china_pressure
            - self.us_support * 0.3
            + self.taiwan_position * 0.2
        )

        if pressure_score >= 5:
            china_strategy = 1
        else:
            china_strategy = 0

        return us_strategy, china_strategy

    def run(self, rounds=100):

        us_matrix, china_matrix = self.game.payoff_matrix()

        us_total = 0
        china_total = 0

        history = []

        for _ in range(rounds):

            # 대부분은 정책 기반 전략
            if random.random() < 0.8:
                us_choice, china_choice = self._choose_strategy()

            # 일부는 불확실성 반영
            else:
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

        risk = calculate_risk(
            self.us_support,
            self.china_pressure,
            self.taiwan_position,
            self.sanctions,
            self.semiconductor,
        )

        shield = silicon_shield_score(
            self.semiconductor,
            self.interdependence,
            self.sanctions,
        )

        economic = calculate_economic_cost(
            risk,
            self.semiconductor,
            self.interdependence,
        )

        equilibria = calculate_nash(
            us_matrix,
            china_matrix
        )

        analysis = generate_analysis(
            risk,
            shield,
            economic,
        )

        return {

            "US Total": us_total,
            "China Total": china_total,

            "US Average": us_total / rounds,
            "China Average": china_total / rounds,

            "Risk": risk,
            "Risk Level": None,

            "Silicon Shield": shield,

            "Economic Cost": economic,

            "Nash": format_equilibria(equilibria),

            "Analysis": analysis,

            "History": history
        }
