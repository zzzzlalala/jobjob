class solution:
    def product1(self, nums):
        out = [1] * len(nums)
        for i in range(1, len(nums)):
            out[i] = out[i - 1] * nums[i - 1]
        temp = 1
        for j in range(len(nums) - 2, -1, -1):
            # print(j)
            temp *= nums[j + 1]
            out[j] *= temp
        return out

    def product2(self, nums):
        length = len(nums)
        L, R, ans = [0] * length, [0] * length, [0] * length
        L[0] = 1
        for i in range(1, length):
            L[i] = nums[i - 1] * L[i - 1]
        R[length - 1] = 1
        for j in range(length - 2, -1, -1):
            R[j] = nums[j + 1] * R[j + 1]
        for i in range(length):
            ans[i] = L[i] * R[i]
        return ans

    def product3(self, nums):
        length = len(nums)
        ans = [1] * length
        ans[0] = 1
        for i in range(1, length):
            ans[i] = nums[i - 1] * ans[i - 1]
        R = 1
        for i in reversed(range(length)):
            ans[i] = ans[i] * R
            R *= nums[i]
        return ans


if __name__ == '__main__':
    solution = solution()
    nums = [1, 2, 3, 4]
    print(solution.product1(nums))
    print(solution.product2(nums))
    print(solution.product3(nums))
