class solution:
    def rob1(self, nums):
        # dp状态缓存(每次偷的最高金额记下来)
        n = len(nums)
        if n == 0:
            return 0
        if n <= 2:
            return max(nums)
        dp = [nums[0], max(nums[0], nums[1])]
        for i in range(2, n):
            dp.append(max(dp[i - 1], dp[i - 2] + nums[i]))
        return max(dp)

    def rob(self, nums):
        # dp空间压缩(前面n-2间房屋的算出来的金额 和 前面n-1 间房屋算出来的金额)
        n = len(nums)
        if n == 0:
            return 0
        if n <= 2:
            return max(nums)
        m1 = nums[0]
        m2 = max(nums[0], nums[1])
        for i in range(2, n):
            m1, m2 = m2, max(m1 + nums[i], m2)
        return m2


if __name__ == '__main__':
    solution = solution()
    nums = [1, 2, 3, 1]
    print(solution.rob(nums))
