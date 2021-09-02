class solution:
    # DP
    def countSubstrings1(self, s):
        ans = 0
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1):
                if s[i] == s[j] and (i - j < 2 or dp[j + 1][i - 1]):
                    dp[j][i] = 1
                    ans += 1
        return ans

    # 中心扩展法
    def countSubstrings2(self, s):
        n = len(s)
        self.ans = 0

        def helper(i, j):
            while i >= 0 and j < n and s[i] == s[j]:
                i -= 1
                j += 1
                self.ans += 1

        for i in range(n):
            helper(i, i)
            helper(i, i + 1)
        return self.ans


if __name__ == '__main__':
    solution = solution()
    # s = "abc"
    s = "aaa"
    print(solution.countSubstrings1(s))
    print(solution.countSubstrings2(s))
