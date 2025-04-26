#!/usr/bin/env python3

# words = ['apple', 'banana', 'cherry']
# uppercase_words = map(str.upper, words)
# uppercase_words = list(uppercase_words)
# print(uppercase_words)

from itertools import groupby
logs = [('2023-10-01', 'System started'),
        ('2023-10-01', 'User logged in'),
        ('2023-10-02', 'Error occurred'),
        ('2023-10-02', 'System rebooted'),
        ('2023-10-02', 'User logged out')
        ]
logs.sort(key=lambda x: x[0])
grouped_logs = groupby(logs, key=lambda x: x[0])
for date, group in grouped_logs:
    print(f"Date: {date}")
    for log in group:
        print(f" - {log[1]}")
