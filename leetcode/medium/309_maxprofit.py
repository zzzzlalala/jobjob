class solution:
    def maxProfit(self, prices):
        if not prices:
            return 0
        f = [[-prices[0], 0, 0]] + [[0] * 3 for _ in range(len(prices) - 1)]
        """
            买入 卖出 冷冻期 买入 卖出 冷冻期
            f[i][0]: 手上持有的股票的最大收益（i-1就有 i买的）       
            f[i][1]：手上不持有股票 处于冷却期（i-1的股票卖了）
            f[i][2]：手上不持有股票 不在冷却期 （i-1没股票的两种情况[1][2]）       
        """
        for i in range(1, len(prices)):
            f[i][0] = max(f[i - 1][0], f[i - 1][2] - prices[i])
            f[i][1] = f[i - 1][0] + prices[i]
            f[i][2] = max(f[i - 1][1], f[i - 1][2])
        return max(f[len(prices) - 1][1], f[len(prices)-1][2])


if __name__ == '__main__':
    solution = solution()
    prices = [1, 2, 3, 0, 2]
    print(solution.maxProfit(prices))
