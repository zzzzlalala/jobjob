class solution:
    def canPartition(self, nums):
        total = sum(nums)
        # 奇数不可能
        if total % 2: return False
        target = total // 2
        dp = [True] + [False] * target
        for i in range(len(nums)):
            for j in range(target, nums[i] - 1, -1):
                # 选不选这个数
                dp[j] = dp[j] or dp[j - nums[i]]
        return dp[-1]


if __name__ == '__main__':
    nums = [1, 5, 11, 5]
    solution = solution()
    print(solution.canPartition(nums))
