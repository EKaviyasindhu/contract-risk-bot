import json
from datetime import datetime
import os

LOG_FILE = "audit_logs/logs.json"


def log_event(filename, overall_risk):
    log = {
        "file_name": filename,
        "timestamp": datetime.now().isoformat(),
        "overall_risk": overall_risk
    }

    os.makedirs("audit_logs", exist_ok=True)

    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            data = json.load(f)
    else:
        data = []

    data.append(log)

    with open(LOG_FILE, "w") as f:
        json.dump(data, f, indent=2)
