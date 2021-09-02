class node:
    def __init__(self, value, step=0):
        self.value = value
        self.step = step


class solution:
    # BFS
    def numSquares1(self, n):
        # 从后往前
        ps = [i * i for i in range(1, int(n ** 0.5) + 1)][::-1]
        pset = set(ps)
        queue, cache = [n], {n: 1}
        while queue:
            val = queue.pop(0)
            if val in pset:
                return cache[val]
            for p in ps:
                if val - p > 0 and val - p not in cache:
                    queue.append(val - p)
                    cache[val - p] = cache[val] + 1
        return -1

    # BFS
    def numSquares2(self, n):
        queue = [node(n)]
        visited = set([node(n).value])

        while queue:
            vertex = queue.pop(0)
            residuals = [vertex.value - i * i for i in range(1, int(n ** 0.5) + 1)[::-1]]
            for i in residuals:
                new_vertex = node(i, vertex.step + 1)
                if i == 0:
                    return new_vertex.step
                elif i not in visited:
                    queue.append(new_vertex)
                    visited.add(i)
        return -1

    # 完全背包DF
    def numSquares3(self, n):
        ps = [i * i for i in range(1, int(n ** 0.5) + 1)][::-1]
        f = [0] + [float('inf')] * n
        for p in ps:
            for j in range(p, n + 1):
                f[j] = min(f[j], f[j - p] + 1)
        return f[-1]

    # 贪心
    def numSquares4(self, n):
        ps = set([i * i for i in range(1, int(n ** 0.5) + 1)])

        def divisible(n, count):
            if count == 1:
                return n in ps
            for p in ps:
                if divisible(n - p, count - 1):
                    return True
            return False

        for count in range(1, n + 1):
            if divisible(n, count):
                return count


if __name__ == '__main__':
    n = 12
    solution = solution()
    print(solution.numSquares1(n))
    print(solution.numSquares2(n))
    print(solution.numSquares3(n))
    print(solution.numSquares4(n))
