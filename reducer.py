#!/usr/bin/env python

import sys

total = 0.0
count = 0

for line in sys.stdin:
    nums = line.strip().split("\t")
    if nums and len(nums) > 1:
        local_sum, local_n = nums
        local_sum = float(local_sum)
        local_n = int(local_n)

        total += local_sum
        count += local_n
    else:
        break

# Calculate the average and print it to the standard output
avg = total / count

print " %s\t%f" % ('average: ', avg)
