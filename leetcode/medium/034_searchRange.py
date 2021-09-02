class solution:
    # 二分
    def searchRange1(self, nums, target):
        if not nums:
            return [-1, -1]

        def binarySearch(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] >= target:
                    right = mid - 1
                else:
                    left = mid + 1
            return left

        start = binarySearch(nums, target)
        end = binarySearch(nums, target + 1) - 1
        if start == len(nums) or nums[start]!=target:
            return [-1, -1]
        else:
            return [start, end]

    # 前后找
    def searchRange2(self, nums, target):
        if not nums:
            return [-1, -1]
        ans = []
        for i in range(len(nums)):
            # print(i)
            if nums[i] == target:
                ans.append(i)
                break
        for j in range(len(nums) - 1, -1, -1):
            # print(j)
            if nums[j] == target:
                ans.append(j)
                break
        return ans

    # 暴力
    def searchRange3(self, nums, target):
        for i in range(len(nums)):
            if nums[i] == target:
                j = i + 1
                while j < len(nums) and nums[j] == target:
                    j += 1
                return [i, j - 1]
        return [-1, -1]


if __name__ == '__main__':
    test = solution()
    nums = [5, 7, 7, 8, 8, 10]
    # nums = [1]
    target = 7
    print(test.searchRange1(nums, target))
    print(test.searchRange2(nums, target))
    print(test.searchRange3(nums, target))
