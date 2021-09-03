class soltion:
    def search(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            tmp  = (right+left) // 2
            # tmp = left + (right - left) // 2
            if nums[tmp] == target:
                return tmp
            if target < nums[tmp]:
                right = tmp - 1
            else:
                left = tmp + 1
        return -1


s = soltion()
nums = [-1, 0, 3, 5, 9, 12]
target = 9
print(s.search(nums, target))
