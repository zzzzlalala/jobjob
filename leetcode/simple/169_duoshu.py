import collections
import random


class solution:
    # sb排序
    def duoshu(self, nums):
        nums.sort()
        return nums[len(nums) // 2]

    # hash映射
    def duoshu2(self, nums):
        counts = collections.Counter(nums)
        # print(counts)
        # print(counts.keys())
        # print(counts.get(1))
        return max(counts.keys(), key=counts.get)

    # 随机化 空间O(1)
    def duoshu3(self, nums):
        final = len(nums) // 2
        while True:
            rad = random.choice(nums)
            if sum(1 for num in nums if num == rad) > final:
                return rad


test = solution()
nums = [2, 2, 1, 1, 1, 2, 2]
print(test.duoshu(nums))
print(test.duoshu2(nums))
print(test.duoshu3(nums))
