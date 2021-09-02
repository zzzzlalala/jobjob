class solution:
    def color(self, nums):
        # 指针
        pre = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i], nums[pre] = nums[pre], nums[i]
                pre += 1
        for i in range(pre, len(nums)):
            if nums[i] == 1:
                nums[i], nums[pre] = nums[pre], nums[i]
                pre += 1
        return nums


if __name__ == '__main__':
    test = solution()
    nums = [2, 0, 2, 1, 1, 0]
    print(sorted(nums))
    print(test.color(nums))
