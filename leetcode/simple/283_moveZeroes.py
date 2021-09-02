class solution:
    def moveZeroes(self, nums):
        if not nums:
            return 0
        j = 0
        for i in range(len(nums)):
            if nums[i] is not 0:
                nums[j] = nums[i]
                j += 1
        for i in range(j, len(nums)):
            nums[i] = 0
        return nums

    # 双指针
    def moveZeroes2(self, nums):
        left = right = 0
        while right < len(nums):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1
        return nums


nums = [0, 1, 0, 3, 12]
test = solution()
print(test.moveZeroes(nums))
print(test.moveZeroes2(nums))
