# 排序数组
import random

"""
    1. 快速排序
    2. 选择排序
"""


class solution:
    """
    # 快速排序
    核心思路：快慢双指针 + 分治
    partition方法
    1.先随机选择一个中间值pivot作为比较的基准，因此比这个基准小的放到左边，比这个基准大的放到右边
    2.把选择的基准放到最左边，也就是nums[low]和nums[pivot]交换位置
    3.慢指针 i 从low位置开始，指向比基准小的数字；快指针 j 从low + 1位置开始遍历
    4.j <= high进入循环：
        如果nums[j]比基准小，nums[i + 1]和nums[j]交换位置，并且i + 1
        j每次循环 + 1
    5.循环结束后，当前 i 指针所在位置即为数组中比base小的最后一个位置，
      将其和最左边的base交换位置，也就是交换nums[low]和nums[i]；
      交换完后，i位置之前的都是比它小的，i位置之后的都是比它大的
    6.返回i，该位置的元素已排序完成，就是已经在它该在的位置了，接下来要排序i之前的和i之后的元素了

    quick_sort方法：
    走一遍partition方法，获取已经排序好的mid
    分别对[low, mid - 1]和[mid + 1, high]两个区间进行排序，也就是mid的左右两边

    """

    def kuaipai(self, nums):
        def partition(low, high):
            pivot = random.randint(low, high)
            nums[low], nums[pivot] = nums[pivot], nums[low]
            i, j = low, low + 1
            while j <= high:
                if nums[j] < nums[low]:
                    nums[i + 1], nums[j] = nums[j], nums[i + 1]
                    i += 1
                j += 1
            nums[low], nums[i] = nums[i], nums[low]
            return i

        def quick_sort(low, high):
            if low < high:
                mid = partition(low, high)
                quick_sort(low, mid - 1)
                quick_sort(mid + 1, high)

        quick_sort(0, len(nums) - 1)
        return nums

    """
    选择排序：
    工作原理，首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置，
    然后，再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。
    以此类推，直到所有元素均排序完毕

    """

    def selection_sort(self, nums):
        n = len(nums)
        for i in range(n):
            for j in range(i, n):
                if nums[i] > nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
        return nums

    """
    冒泡排序：
    冒泡排序时针对相邻元素之间的比较，可以将大的数慢慢“沉底”(数组尾部)
    """

    def maopao(self, nums):
        n = len(nums)
        for c in range(n):
            for i in range(1, n - c):
                if nums[i - 1] > nums[i]:
                    nums[i - 1], nums[i] = nums[i], nums[i - 1]
        return nums

    """
    插入排序：
    前面已排序数组找到插入的位置
    """

    def insert_sort(self, nums):
        n = len(nums)
        for i in range(1, n):
            while i > 0 and nums[i - 1] > nums[i]:
                nums[i - 1], nums[i] = nums[i], nums[i - 1]
                i -= 1
        return nums

    """
    希尔排序:
    相对于插入加一个增量
    """

    def shell_sort(self, nums):
        n = len(nums)
        gap = n // 2
        while gap:
            for i in range(gap, n):
                while i - gap >= 0 and nums[i - gap] > nums[i]:
                    nums[i - gap], nums[i] = nums[i], nums[i - gap]
            gap //= 2
        return nums

    """
    归并排序：
    先将数组分成子序列，让子序列有序，再将子序列间有序，合并成有序数组。
    1.把长度为n的输入序列分成长度 n/2的子序列；
    2.对两个子序列采用归并排序；
    3.合并所有子序列
    """

    def merge_sort(self, nums):
        if len(nums) <= 1:
            return nums

        def merge(left, right):
            res = []
            i, j = 0, 0
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    res.append(left[i])
                    i += 1
                else:
                    res.append(right[j])
                    j += 1
            res += left[i:]
            res += right[j:]
            return res

        mid = len(nums) // 2
        left = self.merge_sort(nums[:mid])
        right = self.merge_sort(nums[mid:])
        return merge(left, right)


s = solution()
nums = [6, 5, 3, 1, 8, 7, 2, 4]
print(s.kuaipai(nums))
print(s.selection_sort(nums))
print(s.maopao(nums))
print(s.insert_sort(nums))
print(s.shell_sort(nums))
print(s.merge_sort(nums))
