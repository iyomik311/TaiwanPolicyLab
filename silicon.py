def silicon_shield_score(
    semiconductor,
    interdependence,
    sanctions
):
    """
    Silicon Shield Index (0~100)

    높을수록 전쟁 억제력이 강함
    """

    score = (
        semiconductor * 0.6
        + interdependence * 0.3
        - sanctions * 0.2
    )

    score = max(0, min(score, 100))

    return round(score, 1)


def shield_level(score):

    if score < 25:
        return "⚪ Weak"

    elif score < 50:
        return "🟡 Moderate"

    elif score < 75:
        return "🟢 Strong"

    return "🔵 Very Strong"
