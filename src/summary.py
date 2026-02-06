def generate_summary(clauses, risks):
    total_clauses = len(clauses)
    risky_clauses = len(risks)

    summary = f"""
This contract contains {total_clauses} clauses.

{risky_clauses} clauses have potential legal risks.

Main risk areas include:
"""

    risk_types = set()
    for clause_risks in risks.values():
        for risk_name, _ in clause_risks:
            risk_types.add(risk_name)

    for r in risk_types:
        summary += f"- {r}\n"

    summary += "\nThis summary is generated to help small businesses understand legal exposure in simple terms."

    return summary
