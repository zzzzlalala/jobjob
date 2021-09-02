import time
class solution:
    # 超时
    def maxProfit(self, prices):
        ans = 0
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                ans = max(ans, prices[j] - prices[i])
        return ans
    def maxProfit1(self,prices):
        min_price  = float('inf')
        max_profit = 0
        for price in prices:
            max_profit = max(price-min_price,max_profit)
            min_price = min(price,min_price)
        return max_profit




if __name__ == '__main__':
    test = solution()
    prices = [7, 1, 5, 3, 6, 4]
    begin = time.time()
    print(test.maxProfit(prices))
    over = time.time()
    begin2 = time.time()
    print(test.maxProfit1(prices))
    over2 = time.time()
    print(over-begin,over2-begin2)
