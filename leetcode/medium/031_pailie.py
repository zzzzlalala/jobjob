class solution:
    """
    1.找一个nums[i] < nums[i+1]
    2.找nums[i] >= nums[j]
    3.替换nums[i] 和 nums[j]
    4.i+1后面反转
    """
    def nextPailie(self, nums):
        # len(nums) = 9 nums[i] =nums[7] nums[i+1]=nums[8]
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        if i >= 0:
            j = len(nums) - 1
            while j > 0 and nums[i] >= nums[j]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]

        left, right = i + 1, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        return nums


if __name__ == '__main__':
    test = solution()
    nums = [1, 2, 3]
    print(test.nextPailie(nums))
