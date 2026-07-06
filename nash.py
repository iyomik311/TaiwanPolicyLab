import nashpy as nash


def calculate_nash(us_matrix, china_matrix):
    """
    미국과 중국의 보수행렬을 받아
    내시균형 목록을 반환한다.
    """

    game = nash.Game(us_matrix, china_matrix)

    equilibria = list(game.support_enumeration())

    return equilibria


def format_equilibria(equilibria):
    """
    화면에 출력하기 좋은 문자열 형태로 변환
    """

    if len(equilibria) == 0:
        return ["No Nash Equilibrium Found"]

    result = []

    for eq in equilibria:
        us_strategy = eq[0]
        china_strategy = eq[1]

        result.append(
            f"US: {us_strategy} | China: {china_strategy}"
        )

    return result
