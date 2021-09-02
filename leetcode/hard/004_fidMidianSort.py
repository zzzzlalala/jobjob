# class solution:
#     def findMedianSort(self, nums1, nums2):


class solution:
    def twosum(self, nums, target):
        hash = dict()
        for i, num in enumerate(nums):
            if target - num in hash:
                return [hash[target - num], i]
            hash[nums[i]] = i
        return []


solution = solution()
nums = [0, 1, 2, 3]
target = 5
print(solution.twosum(nums, target))
