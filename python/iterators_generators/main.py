from iterator import LogFileIterator
from generator import read_logs
from generator import filter_errors
count = 0

logs = read_logs("server.log")

errors = filter_errors(logs)

count = sum(1 for _ in errors)

print(count)
