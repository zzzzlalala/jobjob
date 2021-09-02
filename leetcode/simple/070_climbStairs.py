import time


class solution:
    # 超时
    def climbStairs(self, n):
        if n == 0 or n == 1:
            return 1
        else:
            return self.climbStairs(n - 1) + self.climbStairs(n - 2)

    # 动态
    def climbStairs2(self, n):
        dp = [0] * (n + 1)
        dp[0] = dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[-1]

    def climbStairs3(self, n):
        a = b = 1
        for i in range(2, n + 1):
            a, b = b, a + b
        return b


if __name__ == '__main__':
    test = solution()
    start = time.time()
    print(test.climbStairs(35))
    end = time.time()
    start2 = time.time()
    print(test.climbStairs2(35))
    end2 = time.time()
    print(end - start, 's')
    print(end2 - start2, 's')
    print(test.climbStairs3(35))
