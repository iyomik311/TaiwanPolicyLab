def generate_analysis(risk, shield, economic_cost):
    """
    Generate a policy analysis based on
    simulation indicators.
    """

    text = ""

    # 위험도
    if risk >= 80:
        text += "🔴 Military tension is extremely high.\n\n"

    elif risk >= 60:
        text += "🟠 Military tension is increasing.\n\n"

    else:
        text += "🟢 Military tension remains relatively stable.\n\n"

    # 실리콘 실드
    if shield >= 75:
        text += (
            "🛡 Taiwan's semiconductor industry provides a strong "
            "deterrent against military conflict.\n\n"
        )

    elif shield >= 50:
        text += (
            "🛡 Semiconductor dependence provides a moderate "
            "deterrent effect.\n\n"
        )

    else:
        text += (
            "🛡 The Silicon Shield effect is relatively weak.\n\n"
        )

    # 경제 비용
    if economic_cost >= 70:
        text += (
            "💰 A military conflict would cause severe economic losses.\n\n"
        )

    elif economic_cost >= 40:
        text += (
            "💰 Conflict would significantly disrupt global trade.\n\n"
        )

    else:
        text += (
            "💰 Estimated economic damage is relatively limited.\n\n"
        )

    # 종합 평가
    if risk >= 80 and shield >= 70:
        text += (
            "📘 Overall Assessment:\n"
            "Although military tension is high, strong global dependence "
            "on Taiwan's semiconductor industry raises the cost of war. "
            "This reflects the concept of the Silicon Shield."
        )

    elif risk >= 80:
        text += (
            "📘 Overall Assessment:\n"
            "The current policy combination creates a high probability of "
            "military escalation."
        )

    elif risk >= 60:
        text += (
            "📘 Overall Assessment:\n"
            "The situation resembles strategic competition with increasing "
            "pressure on all actors."
        )

    else:
        text += (
            "📘 Overall Assessment:\n"
            "The strategic environment remains relatively stable."
        )

    return text
