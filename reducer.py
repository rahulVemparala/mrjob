
import sys

total = 0.0
count = 0

for line in sys.stdin:
    num, cnt = line.strip().split("\t")
    total += float(num)
    count += int(cnt)

avg = total / count
print("Average: {0:.2f}".format(avg))
