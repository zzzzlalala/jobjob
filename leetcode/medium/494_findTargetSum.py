class solution:
    # 零钱问题（完全背包）最少的那个
    def coinChange(self, coins, amount):
        dp = [float("inf")] * (amount + 1)

        dp[0] = 0
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)

        return dp[-1] if dp[-1] != float("inf") else -1

    # 零钱问题（完全背包组合） 多少组合
    def coinChange2(self, coins, amount):
        dp = [0] * (amount + 1)
        # 啥也不选也是一种方法
        dp[0] = 1
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]
        return dp[-1]

    # target +- 问题（01背包） 多少组合
    def findTargetSum(self, nums, target):
        nums_sum = sum(nums)
        if target > nums_sum or (target + nums_sum) % 2:
            return 0
        positive_sum = (nums_sum + target) // 2
        dp = [0 for _ in range(positive_sum + 1)]
        dp[0] = 1
        for num in nums:
            for i in range(positive_sum, num - 1, -1):
                dp[i] += dp[i - num]
        return dp[-1]


s = solution()
ans = s.findTargetSum(nums=[1, 1, 1, 1, 1], target=3)
ans2 = s.coinChange(coins=[1, 2, 5], amount=11)
ans3 = s.coinChange2(amount=3, coins=[2])
print(ans)
print(ans2)
print(ans3)
