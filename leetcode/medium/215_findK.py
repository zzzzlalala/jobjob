import heapq
import random


def heapsort(item):
    h = []
    for value in item:
        heapq.heappush(h, value)
    return [heapq.heappop(h) for i in range(len(h))]


class solution:
    def findKth1(self, nums, k):
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]

    def findKth2(self, nums, k):
        # 快速排序(双指针+分治)
        def findTopKth(left, right):
            pivot = random.randint(left, right)
            nums[left], nums[pivot] = nums[pivot], nums[left]
            base = nums[left]
            i = left
            j = left + 1
            while j <= right:
                if nums[j] > base:
                    nums[i + 1], nums[j] = nums[j], nums[i + 1]
                    i += 1
                j += 1
            nums[left], nums[i] = nums[i], nums[left]
            if i == k - 1:
                return nums[i]
            elif i > k - 1:
                return findTopKth(left, i - 1)
            else:
                return findTopKth(i + 1, right)

        return findTopKth(0, len(nums) - 1)


if __name__ == '__main__':
    solution = solution()
    nums = [3, 2, 1, 5, 6, 4]
    # print(heapsort(nums))
    k = 2
    print(solution.findKth1(nums, k))
    print(solution.findKth2(nums, k))

# heapq函数(堆排序)

# random
list = []
name = ["zhang", "wang", "cao", "li"]
for i in range(len(name)):
    choice_name = random.choice(name)
    name.remove(choice_name)
    list.append(choice_name)
print(list)
