class solution:
    def twosum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

    def twosum1(self, nums, target):
        dict = {}
        for i, num in enumerate(nums):
            if target - num in dict:
                return dict[[target - num], i]
            dict[num] = i

    def twosum2(self, nums, target):
        hash = dict()
        for i, num in enumerate(nums):
            if target - num in hash:
                return [hash[target - num], i]
            hash[nums[i]] = i
        return []


# test
nums = [2, 7, 7, 19]
target = 10
test = solution()
print(test.twosum(nums, target))
print(test.twosum1(nums, target))
print(test.twosum2(nums, target))
