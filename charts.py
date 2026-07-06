import matplotlib.pyplot as plt


def plot_average_scores(results):
    """
    미국과 중국의 평균 보수를 막대그래프로 표시
    """

    labels = ["United States", "China"]
    scores = [
        results["US Average"],
        results["China Average"]
    ]

    fig, ax = plt.subplots(figsize=(6,4))

    ax.bar(labels, scores)

    ax.set_ylabel("Average Payoff")
    ax.set_title("Average Payoff Comparison")

    return fig


def plot_total_scores(results):
    """
    총 보수를 막대그래프로 표시
    """

    labels = ["United States", "China"]
    totals = [
        results["US Total"],
        results["China Total"]
    ]

    fig, ax = plt.subplots(figsize=(6,4))

    ax.bar(labels, totals)

    ax.set_ylabel("Total Payoff")
    ax.set_title("Total Payoff Comparison")

    return fig
