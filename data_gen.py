import numpy as np


with open('nums.txt', 'w') as f:
    for i in range(100):
        length = np.random.randint(1, 50)
        nums = np.arange(2, length)
        nums = [str(x) for x in nums]
        nums_formatted = ' '.join(nums) + "\n"
        f.write(nums_formatted)
    