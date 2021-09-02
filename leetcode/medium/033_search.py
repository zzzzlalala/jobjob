class solution:
    def search(self, nums, target):
        if not nums:
            return -1
        L, R = 0, len(nums) - 1
        while L <= R:
            mid = (L + R) // 2
            if nums[mid] == target:
                return mid
            if nums[0] <= nums[mid]:
                if nums[0] <= target < nums[mid]:
                    R = mid - 1
                else:
                    L = mid + 1
            else:
                if nums[mid] < target <= nums[len(nums) - 1]:
                    L = mid + 1
                else:
                    R = mid - 1
        return -1


if __name__ == '__main__':
    test = solution()
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 0
    print(test.search(nums, target))
