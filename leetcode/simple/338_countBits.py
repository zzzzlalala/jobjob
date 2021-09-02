class solution:

    # zz
    def countBits1(self, n):
        res = []
        for i in range(n + 1):
            res.append(bin(i).count('1'))
        return res

    # Brian Kernighan
    '''
        原理
        对于任意整数 X ，令 X = X &(X-1),该运算将 X 的二进制表示的最后一个 1 变成 0
    '''

    def countBits2(self, n):
        bits = [self.countOnes(i) for i in range(n + 1)]
        return bits

    def countOnes(self, x):
        ones = 0
        while x > 0:
            x = x & (x - 1)
            ones += 1
        return ones

    # 动态规划-最低设置位
    def countBits3(self, n):
        bits = [0]
        for i in range(1, n + 1):
            bits.append(bits[i & i - 1] + 1)
        return bits


if __name__ == '__main__':
    test = solution()
    print(test.countBits1(5))
    print(test.countBits2(5))
    print(test.countBits3(5))
