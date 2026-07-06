def generate_analysis(
    risk,
    economic_cost,
    silicon_score
):
    """
    정책 분석 결과 생성
    """

    analysis = []

    # 긴장도 분석
    if risk >= 80:
        analysis.append(
            "🔴 Military tension is extremely high."
        )
    elif risk >= 60:
        analysis.append(
            "🟠 Military tension is increasing."
        )
    else:
        analysis.append(
            "🟢 Military tension remains relatively stable."
        )

    # 경제 비용 분석
    if economic_cost >= 70:
        analysis.append(
            "💰 The expected economic cost of conflict is severe."
        )
    elif economic_cost >= 40:
        analysis.append(
            "💰 Conflict would impose significant economic losses."
        )
    else:
        analysis.append(
            "💰 Economic losses are comparatively limited."
        )

    # 실리콘 실드 분석
    if silicon_score >= 75:
        analysis.append(
            "🛡 Strong semiconductor dependence creates a powerful deterrent against war."
        )
    elif silicon_score >= 50:
        analysis.append(
            "🛡 The semiconductor industry provides a moderate deterrent effect."
        )
    else:
        analysis.append(
            "🛡 The deterrent effect of the semiconductor industry is weak."
        )

    # 종합 평가
    if risk >= 80 and silicon_score >= 70:
        analysis.append(
            "📘 Although military tension is high, strong economic interdependence discourages full-scale conflict."
        )

    elif risk >= 80:
        analysis.append(
            "📘 Current conditions suggest a serious risk of military escalation."
        )

    elif risk >= 60:
        analysis.append(
            "📘 The situation resembles a strategic competition with growing tension."
        )

    else:
        analysis.append(
            "📘 Current policies support a relatively stable strategic environment."
        )

    return analysis
