class solution:
    """
    # 排序+双指针
        1.特判，对于数组长度 n，如果数组为 null 或者数组长度小于 3，返回 []。
        2.对数组进行排序。
        3.遍历排序后数组：
            * 若 nums[i]>0：因为已经排序好，所以后面不可能有三个数加和等于 0，直接返回结果。
            * 对于重复元素：跳过，避免出现重复解
            * 令左指针 L=i+1，右指针 R=n-1，当 L<R 时，执行循环：
                当 nums[i]+nums[L]+nums[R]==0，执行循环，
                判断左界和右界是否和下一位置重复，去除重复解。
                并同时将 L,R 移到下一位置，寻找新的解

                若和大于 0，说明 nums[R] 太大，R 左移
                若和小于 0，说明 nums[L] 太小，L 右移

    """
    def threeSum(self, nums):
        n = len(nums)
        if (not nums or n < 3):
            return []
        nums.sort()
        res = []
        for i in range(n):
            if (nums[i] > 0):
                return res
            if (i > 0 and nums[i] == nums[i - 1]):
                # 重复跳过
                continue
            left = i + 1
            right = n - 1
            while (left < right):
                if (nums[i] + nums[left] + nums[right] == 0):
                    res.append([nums[i], nums[left], nums[right]])
                    # 判断去除重复解
                    while (left < right and nums[left] == nums[left + 1]):
                        left = left + 1
                    while (left < right and nums[right] == nums[right - 1]):
                        right = right - 1
                    left = left + 1
                    right = right - 1
                elif (nums[i] + nums[left] + nums[right] > 0):
                    right = right - 1
                else:
                    left = left + 1
        return res


if __name__ == '__main__':
    test = solution()
    nums = [-1, 0, 1, 2, -1, -4]
    print(test.threeSum(nums))
