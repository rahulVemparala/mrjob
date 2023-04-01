#!/usr/bin/env python
import sys

local_sum = 0
local_n = 0

for line in sys.stdin:
    nums = line.strip().split()
    if nums:
        nums = [int(x) for x in nums]
        local_sum += sum(nums)
        local_n += len(nums)
    else:
        break


print "%d\t%d" % (local_sum, local_n)
