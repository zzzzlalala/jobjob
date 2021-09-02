class solution:
    def permute(self, nums):
        # 回溯
        def backtrack(first=0):

            if first == len(nums):
                ans.append(nums[:])
            for i in range(first, len(nums)):
                nums[first], nums[i] = nums[i], nums[first]
                backtrack(first + 1)
                nums[first], nums[i] = nums[i], nums[first]

        ans = []
        backtrack()
        return ans


if __name__ == '__main__':
    test = solution()
    nums = [1, 2, 3]
    # print(nums[:])
    print(test.permute(nums))
