import re


def split_clauses(text):
    """
    Splits contract text into clauses based on numbering patterns
    """
    clauses = {}
    current_clause = "Introduction"
    clauses[current_clause] = ""

    lines = text.split("\n")

    for line in lines:
        line = line.strip()
        if not line:
            continue

        # Match clause numbers like 1., 1.1, 2.3.4
        if re.match(r"^\d+(\.\d+)*\s", line):
            current_clause = line.split(" ", 1)[0]
            clauses[current_clause] = line
        else:
            clauses[current_clause] += " " + line

    return clauses
