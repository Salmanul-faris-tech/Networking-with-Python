import re
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

def load_logs(file_path):
    log_pattern = r"(?P<date>[A-Za-z]{3} \d{1,2} \d{2}:\d{2}:\d{2}) (?P<host>\S+) (?P<service>\w+)\((?P<module>\w+)\)\[(?P<pid>\d+)\]: (?P<message>.+)"
    logs = []
    with open(file_path, "r") as file:
        for line in file:
            match = re.match(log_pattern, line)
            if match:
                log_data = match.groupdict()
                log_data["datetime"] = datetime.strptime(log_data["date"], "%b %d %H:%M:%S")
                logs.append(log_data)
    return logs

print("Enter log filename")
path = input()

logs = load_logs(path)

log_df = pd.DataFrame(logs)

log_df["hour"] = log_df["datetime"].dt.hour

hourly_activity = log_df.groupby("hour").size()

# Log Activity by Hour of the Day
plt.figure(figsize=(10, 6))
hourly_activity.plot(kind="bar", color="skyblue", edgecolor="black")
plt.title("Log Activity by Hour of the Day", fontsize=14)
plt.xlabel("Hour of the Day", fontsize=12)
plt.ylabel("Number of Logs", fontsize=12)
plt.xticks(rotation=0)
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()
plt.show()

print("\nHourly Log Activity:\n", hourly_activity)
