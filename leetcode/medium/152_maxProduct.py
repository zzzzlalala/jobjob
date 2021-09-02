class solution:
    def maxProduct(self, nums):
        max_num, min_num = nums[0], nums[0]
        ans = nums[0]
        for i in range(1, len(nums)):
            temp_max = max_num
            temp_min = min_num
            max_num = max(temp_max * nums[i], nums[i], temp_min * nums[i])
            min_num = min(temp_min * nums[i], nums[i], temp_max * nums[i])
            ans = max(max_num, ans)
        return ans


if __name__ == '__main__':
    solution = solution()
    nums = [2, 3, -2, 4]
    print(solution.maxProduct(nums))
