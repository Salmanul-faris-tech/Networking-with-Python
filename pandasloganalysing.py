import pandas as pd
import re

with open("linux.log", "r") as file:
    lines = file.readlines()

log_pattern = r"(?P<date>[A-Za-z]{3} \d{1,2} \d{2}:\d{2}:\d{2}) (?P<host>\S+) (?P<service>\w+)\((?P<module>\w+)\)\[(?P<pid>\d+)\]: (?P<message>.+)"
logs = [re.match(log_pattern, line).groupdict() for line in lines if re.match(log_pattern, line)]

log_df = pd.DataFrame(logs)

print("Parsed Logs:\n", log_df.head())


