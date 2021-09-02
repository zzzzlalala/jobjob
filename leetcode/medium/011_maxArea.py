class solution:
    """
        双指针：
            1.两个指针指向的数字中较小值∗指针之间的距离；
            2.哪边小哪边向中间移动
    """
    def maxArea(self, height):
        left, right = 0, len(height) - 1
        ans = 0
        while left < right:
            area = min(height[left], height[right]) * (right - left)
            ans = max(ans, area)
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return ans


if __name__ == '__main__':
    test = solution()
    height = [4,3,2,1,4]
    print(test.maxArea(height))
