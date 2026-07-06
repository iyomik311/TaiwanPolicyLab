def calculate_economic_cost(
    risk,
    semiconductor,
    interdependence
):
    """
    Estimate Economic Cost (%)
    """

    cost = (
        risk * 0.5
        + semiconductor * 0.3
        + interdependence * 0.4
    )

    cost = min(cost, 100)

    return round(cost, 1)


def economic_level(cost):

    if cost < 25:
        return "🟢 Low"

    elif cost < 50:
        return "🟡 Moderate"

    elif cost < 75:
        return "🟠 High"

    return "🔴 Severe"
