# 异或
from functools import reduce
"""
    reduce()函数
    reduce(function, iterable[, initializer])
    count()函数
    str.count(sub,start=0,end=len(string)
"""

class solution:
    def singleNumber(self, nums):
        return reduce(lambda x, y: x ^ y, nums)

    def hanmingDistance(self, x, y):
        # 汉明距离：两个数字对应二进制不同位置的数目
        return bin(x ^ y).count('1')


if __name__ == '__main__':
    test = solution()
    nums = [4, 1, 2, 1, 2]
    print(test.singleNumber(nums))

    x = 3
    y = 1
    print(test.hanmingDistance(x, y))
