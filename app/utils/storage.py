import json

from datetime import datetime


def daily_brief(data):

    timestamp = datetime.now().strftime(
        "%Y-%m-%d_%H-%M-%S"
    )

    filename = f"data/brief_{timestamp}.json"

    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

    return filename