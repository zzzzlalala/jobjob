class solution:
    # sb
    def findNum(self, nums):
        while nums:
            for i in range(len(nums)):
                for j in range(len(nums)):
                    if nums[i] == nums[j] and i != j:
                        return nums[i]
        return 0

    # set()
    def findNum1(self, nums):
        s = set()
        for num in nums:
            if num in s:
                return num
            else:
                s.add(num)

    # 二分
    def findNum2(self, nums):
        left = 1
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            count = 0
            for num in nums:
                if num <= mid:
                    count += 1
            if count <= mid:
                left = mid + 1
            else:
                right = mid
        return left

    # 快慢指针
    def findNum3(self, nums):
        slow = fast = circle_start = 0
        while (1):
            fast = nums[nums[fast]]
            slow = nums[slow]
            if fast == slow:
                break
        while (1):
            slow = nums[slow]
            circle_start = nums[circle_start]
            if circle_start == slow:
                return slow


if __name__ == '__main__':
    solution = solution()
    nums = [1, 3, 4, 2, 2]
    print(solution.findNum(nums))
    print(solution.findNum1(nums))
    print(solution.findNum2(nums))
    print(solution.findNum3(nums))
