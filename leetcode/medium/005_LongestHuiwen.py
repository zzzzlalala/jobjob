class solution:
    # 动态规划
    """
        回文：(去掉一前一后还是回文)
            P(i,j) = P(i+1,j-1) ∩ (s[i] == s[i+1])
            1个：P(i,i) = True
            2个：P(i,i+1) = s[i]==s[i+1]

    """

    def LongestHuiwen(self, s):

        n = len(s)
        if n < 2:
            return s
        max_len = 1
        begin = 0
        P = [[False] * n for _ in range(n)]
        for i in range(n):
            P[i][i] = True
        for left in range(2, n + 1):
            for i in range(n):
                j = left + i - 1
                if j >= n:
                    break
                if s[i] != s[j]:
                    P[i][j] = False
                else:
                    if j - i < 3:
                        P[i][j] = True
                    else:
                        P[i][j] = P[i + 1][j - 1]
                if P[i][j] and j - i + 1 > max_len:
                    max_len = j - i + 1
                    begin = i
            return s[begin:begin + max_len]

    # 中心扩展法
    """
        P(i,j)←P(i+1,j−1)←P(i+2,j−2)←⋯←某一边界情况
    """

    def expandAroundCenter(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1

    def LongestHuiwen1(self, s):
        start, end = 0, 0
        for i in range(len(s)):
            left1, right1 = self.expandAroundCenter(s, i, i)
            left2, right2 = self.expandAroundCenter(s, i, i + 1)
            if right1 - left1 > end - start:
                start, end = left1, right1
            if right2 - left2 > end - start:
                start, end = left2, right2
        return s[start:end + 1]


if __name__ == '__main__':
    test = solution()
    s = 'babad'
    print(test.LongestHuiwen(s))
    print(test.LongestHuiwen1(s))
