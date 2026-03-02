import json
from datetime import datetime

FILE = "progress.json"

def track(problem):

    today = str(datetime.now().date())

    data = {
        "date": today,
        "problem": problem["name"]
    }

    with open(FILE, "a") as f:
        f.write(json.dumps(data) + "\n")