import collections


class solution:
    # 前缀和
    def subSum(self, nums, k):
        map = collections.Counter({0: 1})
        pre_sum = 0
        ans = 0
        for num in nums:
            pre_sum += num
            ans += map[pre_sum - k]
            map[pre_sum] += 1
        return ans


if __name__ == '__main__':
    solution = solution()
    nums = [1, 1, 1]
    k = 2
    print(solution.subSum(nums, k))
