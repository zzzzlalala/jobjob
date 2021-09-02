class solution:
    def wordBreak1(self, s, wordDict):
        # 动态规划
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(n):
            for j in range(i + 1, n + 1):
                if (dp[i] and (s[i:j] in wordDict)):
                    dp[j] = True
        return dp[-1]

    def wordBreak2(self, s, wordDict):
        # 回溯使用缓存机制
        
        import functools
        @functools.lru_cache(None)
        def backTrack(s):
            if not s:
                return True
            ans = False
            for i in range(1, len(s) + 1):
                if (s[:i] in wordDict):
                    ans = backTrack(s[i:]) or ans
            return ans

        return backTrack(s)


if __name__ == '__main__':
    solution = solution()
    s = "leetcode"
    wordDict = ["leet", "code"]
    print(solution.wordBreak1(s, wordDict))
    print(solution.wordBreak2(s, wordDict))
