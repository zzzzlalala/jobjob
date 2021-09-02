# 动态规划
# dp{i} = max{nums[i],dp[i-1]+nums[i]}

class solution:
    def maxSubArray(self, nums):
        size = len(nums)
        if size == 0:
            return 0
        dp = [0 for _ in range(size)]

        dp[0] = nums[0]
        for i in range(1, size):
            if dp[i - 1] >= 0:
                dp[i] = dp[i - 1] + nums[i]
            else:
                dp[i] = nums[i]
        return max(dp)

class solution2:
    def maxSubArray(self,nums):
        size = len(nums)
        pre = 0
        res = nums[0]
        for i in range(size):
            pre = max(nums[i],pre+nums[i])
            res = max(res,pre)
        return res

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
test = solution()
test2 = solution2()
print(test.maxSubArray(nums))
print(test2.maxSubArray(nums))
