class solution:
    # 排序比对
    def findUnsortedSub1(self, nums):
        new_nums = sorted(nums)
        left, right = 0, len(nums) - 1
        while left < len(nums):
            if nums[left] != new_nums[left]:
                break
            left += 1
        if left == len(nums):
            return 0
        while right > left:
            if nums[right] != new_nums[right]:
                break
            right -= 1
        return right - left + 1

    # 双遍历
    def findUnsortedSub2(self, nums):
        n = len(nums)
        max_num = nums[0]
        right = 0
        for i in range(n):
            if nums[i] >= max_num:
                max_num = nums[i]
            else:
                right = i
        left = n
        min_nums = nums[-1]
        for i in range(n - 1, -1, -1):
            if nums[i] <= min_nums:
                min_nums = nums[i]
            else:
                left = i
        return 0 if left == right else right - left + 1


if __name__ == '__main__':
    solution = solution()
    nums = [2, 6, 4, 8, 10, 9, 15]
    print(solution.findUnsortedSub1(nums))
    print(solution.findUnsortedSub2(nums))
