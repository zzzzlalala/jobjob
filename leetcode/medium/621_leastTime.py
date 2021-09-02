import collections


class solution:
    def leastTime1(self, tasks, n):
        freq = collections.Counter(tasks)
        m = len(freq)
        nextValid = [1] * m
        rest = list(freq.values())

        time = 0
        for i in range(len(tasks)):
            time += 1
            minNextValid = min(nextValid[j] for j in range(m) if rest[j] > 0)
            time = max(time, minNextValid)

            best = -1
            for j in range(m):
                if rest[j] and nextValid[j] <= time:
                    if best == -1 or rest[j] > rest[best]:
                        best = j
            nextValid[best] = time + n + 1
            rest[best] -= 1
        return time

    def leastTime2(self, tasks, n):
        freq = collections.Counter(tasks)
        maxExex = max(freq.values())
        # maxCount为一共有多少个任务和出现最多的那个任务出现次数一样 A3次 B也3次 maxCount= 2
        maxCount = sum(1 for v in freq.values() if v == maxExex)
        return max((maxExex - 1) * (n + 1) + maxCount, len(tasks))

    def leastTime3(self, tasks, n):
        length = len(tasks)
        if length <= 1:
            return length
        # 记录次数
        tasks_map = dict()
        for task in tasks:
            tasks_map[task] = tasks_map.get(task, 0) + 1
        # 按任务出现最多排序
        tasks_sort = sorted(tasks_map.items(), key=lambda x: x[1], reverse=True)
        # 出现最多任务次数
        max_tasks_count = tasks_sort[0][1]
        # 至少需要最短时间
        ans = (max_tasks_count - 1) * (n + 1)
        for sort in tasks_sort:
            if sort[1] == max_tasks_count:
                ans += 1
        return ans if ans >= length else length

    def leastTime4(self, tasks, n):
        """
     1. 计算每个任务出现的次数.
     2. 找出出现次数最多的任务，假设出现次数为 x.
     3. x - 1是可以划分的Block数，每个block长度为n + 1. 所以计算至少需要的时间 (x - 1) * (n + 1)，记为 min_time.
     4. 计算出现次数为 x 的任务总数 count，计算最终结果为 min_time + count.
     5. 特殊情况:AAABBBCCDD，n = 2, 这种情况不存在空闲时间，应该返回任务长度

         """
        counter = collections.Counter(tasks)
        x = max(counter.values())
        min_time = (x - 1) * (n + 1)
        for key in counter:
            if counter[key] == x:
                min_time += 1
        return max(min_time, len(tasks))


if __name__ == '__main__':
    solution = solution()
    tasks = ["A", "A", "A", "B", "B", "B"]
    n = 2
    print(solution.leastTime1(tasks, n))
    print(solution.leastTime2(tasks, n))
    print(solution.leastTime3(tasks, n))
    print(solution.leastTime4(tasks, n))
