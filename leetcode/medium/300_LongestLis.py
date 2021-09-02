class solution:
    # DP
    def LongestLis(self, nums):
        if not nums:
            return 0
        dp = []
        for i in range(len(nums)):
            dp.append(1)
            # print(dp)
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)


if __name__ == '__main__':
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    solution = solution()
    print(solution.LongestLis(nums))
