import collections
import heapq
import random


class solution:
    # 直接排序
    # def topKFreq1(self, nums, k):
    #     count = collections.Counter(nums)
    #     return [item[0] for item in count.most_common(k)]

    # 堆排序
    def topKFreq2(self, nums, k):
        count = collections.Counter(nums)
        heap = [(key, val) for key, val in count.items()]
        return [item[1] for item in heapq.nlargest(k, heap)]

    # 堆排序2
    # def topKFreq3(self, nums, k):
    #     count = collections.Counter(nums)
    #     heap = []
    #     for key, val in count.items():
    #         if len(heap) >= k:
    #             if val > heap[0][0]:
    #                 heapq.heapreplace(heap, (val, key))
    #         else:
    #             heapq.heappush(heap, (val, key))
    #     return [item[1] for item in heap]

    # # 快排
    # def topKFreq4(self, nums, k):
    #     count = collections.Counter(nums)
    #     nums_new = list(count.items())
    #     topKs = self.findKth2(nums_new, k, 0, len(nums_new) - 1)
    #     return [item[0] for item in topKs]
        # 快速排序(双指针+分治)

    # def findKth2(self, nums_new, k, left, right):
    #     pivot = random.randint(left, right)
    #     nums_new[left], nums_new[pivot] = nums_new[pivot], nums_new[left]
    #     base = nums_new[left][1]
    #     i = left
    #     for j in range(left + 1, right + 1):
    #         if nums_new[j][1] > base:
    #             nums_new[i + 1], nums_new[j] = nums_new[j], nums_new[i + 1]
    #             i += 1
    #     nums_new[left], nums_new[i] = nums_new[i], nums_new[left]
    #     if i == k - 1:
    #         return nums_new[:k]
    #     elif i > k - 1:
    #         return self.findKth2(nums_new, k, left, i - 1)
    #     else:
    #         return self.findKth2(nums_new, k, i + 1, right)


if __name__ == '__main__':
    solution = solution()
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    # print(solution.topKFreq1(nums, k))
    print(solution.topKFreq2(nums, k))
    # print(solution.topKFreq3(nums, k))
    # print(solution.topKFreq4(nums, k))
