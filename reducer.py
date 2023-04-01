import sys

grand_total = 0
grand_number = 0

for line in sys.stdin:
    try:
        line = line.strip()
        if line:
            total, num = line.split('\t')
            grand_total += total
            grand_number += num
        else:
            break

    except ValueError:
        continue

average = float(grand_total) / grand_number
print '%s\t%f' % ('Grand average', average)
