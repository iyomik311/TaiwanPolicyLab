def calculate_risk(
    us_support,
    china_pressure,
    taiwan_position,
    sanctions,
    semiconductor
):
    """
    Escalation Risk Score (0~100)
    """

    risk = (
        us_support * 3
        + china_pressure * 4
        + taiwan_position * 2
        + sanctions * 2
        - semiconductor * 0.2
    )

    risk = max(0, min(100, risk))

    return round(risk, 1)


def risk_level(score):

    if score < 30:
        return "🟢 Stable"

    elif score < 60:
        return "🟡 Tension"

    elif score < 80:
        return "🟠 Crisis"

    return "🔴 Conflict"
