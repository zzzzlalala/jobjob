class solution:
    def twoSum1(self, nums, target):
        n = len(nums)
        res = []
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    res.append([i, j])
        return res

    def twoSum2(self, nums, target):
        hashtable = dict()
        for i, num in enumerate(nums):
            if target - num in nums:
                return [hashtable[target - num], i]
            hashtable[nums[i]] = i

        return []


s = solution()
nums = [4, 5, 11, 15]
target = 9
print(s.twoSum1(nums, target))
print(s.twoSum2(nums, target))
