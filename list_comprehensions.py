#!/usr/bin/env python3
# square_evens = [x**2 for x in range(1, 20) if x % 2 == 0]
# print(square_evens)


log_file = open('/home/fretagi/Documents/scripts/playground/Xorg.0.log', 'r')
keyword = 'error'
keyword_lines = (line.strip() for line in log_file if keyword in line)
for line in keyword_lines:
    print(line)
log_file.close()
