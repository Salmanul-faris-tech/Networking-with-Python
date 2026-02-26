import linecache
import re

counter = 0
with open("auth.log", "r") as file:
    for line in file:
        counter += 1

pattern = re.compile(
    r'^(?P<timestamp>\w+\s+\d+\s+\d+:\d+:\d+).*'
    r'(?P<message>Failed password for (?:invalid user )?\S+)\s+'
    r'from (?P<ip>\d+\.\d+\.\d+\.\d+) '
    r'port (?P<port>\d+)'
)

i = 1

while i <= counter:
    content = linecache.getline('auth.log',i)
    match = pattern.search(content)
    if match:
        print(
            f"[LINE {i}] "
            f"Timestamp: {match.group('timestamp')} | "
            f"Message: \"{match.group('message')}\" | "
            f"IP: {match.group('ip')} | "
            f"Port: {match.group('port')}"
        )
    i +=1