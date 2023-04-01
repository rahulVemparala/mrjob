import sys

total = 0
num = 0
for line in sys.stdin:
    nums = line.strip().split()
    if nums:
        nums = [int(x) for x in nums]
        total += sum(nums)
        nums += len(nums)

    else:
        print("breaking ")
        break

# print(f"total: {sum(nums)}, num of observations : {len(nums)}")
print '%d\t%d' % (sum(nums), len(nums))
