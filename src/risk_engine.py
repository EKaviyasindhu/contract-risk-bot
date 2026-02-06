def detect_risks(clauses):
    """
    Detects risky clauses using keyword-based rules
    """
    risk_results = {}

    for clause_id, text in clauses.items():
        text_lower = text.lower()
        risks = []

        if "indemnity" in text_lower or "indemnify" in text_lower:
            risks.append(("Indemnity Clause", "High"))

        if "penalty" in text_lower or "liquidated damages" in text_lower:
            risks.append(("Penalty Clause", "Medium"))

        if "terminate at any time" in text_lower or "unilateral termination" in text_lower:
            risks.append(("Unilateral Termination", "High"))

        if "auto-renew" in text_lower or "automatic renewal" in text_lower:
            risks.append(("Auto-Renewal", "Medium"))

        if "non-compete" in text_lower or "non compete" in text_lower:
            risks.append(("Non-Compete Clause", "High"))

        if "jurisdiction" in text_lower or "governing law" in text_lower:
            risks.append(("Jurisdiction Clause", "Low"))

        if risks:
            risk_results[clause_id] = risks

    return risk_results

def calculate_overall_risk(risks):
    score_map = {"Low": 1, "Medium": 2, "High": 3}

    if not risks:
        return "Low"

    total = 0
    count = 0

    for clause_risks in risks.values():
        for _, level in clause_risks:
            total += score_map[level]
            count += 1

    avg_score = total / count

    if avg_score >= 2.5:
        return "High"
    elif avg_score >= 1.5:
        return "Medium"
    else:
        return "Low"