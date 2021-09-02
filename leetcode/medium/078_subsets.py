class solution:

    def subsets1(self, nums):
        # 迭代
        ans = [[]]
        for i in nums:
            ans = ans + [[i] + num for num in ans]
        return ans

    def subsets2(self, nums):
        # 递归
        ans = []
        path = []

        def backtrack(nums, start):
            ans.append(path[:])
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(nums, i + 1)
                path.pop()

        backtrack(nums, 0)
        return ans


if __name__ == '__main__':
    test = solution()
    nums = [1, 2, 3]
    print(test.subsets1(nums))
    print(test.subsets2(nums))
