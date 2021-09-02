from collections import deque


class solution:
    # 广度优先
    def canFinish1(self, numsCourses, prerequisites):
        # 入度表
        indegree = [0 for _ in range(numsCourses)]
        # print(indegree)
        # 邻接表
        adjacency = [[] for _ in range(numsCourses)]
        # print(adjacency)
        queue = deque()
        for cur, pre in prerequisites:
            indegree[cur] += 1
            adjacency[pre].append(cur)
        for i in range(len(indegree)):
            if not indegree[i]:
                queue.append(i)
        while queue:
            pre = queue.popleft()
            numsCourses -= 1
            for cur in adjacency[pre]:
                indegree[cur] -= 1
                if not indegree[cur]:
                    queue.append(cur)
        return not numsCourses

    # DFS
    def canFinish2(self, numCourses, prerequisites):
        def dfs(i, adjacency, flags):
            if flags[i] == -1:
                return True
            if flags[i] == 1:
                return False
            flags[i] = 1
            for j in adjacency[i]:
                if not dfs(j, adjacency, flags):
                    return False
            flags[i] = -1
            return True

        adjacency = [[] for _ in range(numCourses)]
        flags = [0 for _ in range(numCourses)]
        for cur, pre in prerequisites:
            adjacency[pre].append(cur)
        for i in range(numCourses):
            if not dfs(i, adjacency, flags):
                return False
        return True


if __name__ == '__main__':
    solution = solution()
    numCourses = 2
    prerequisites = [[1, 0]]
    print(solution.canFinish1(numCourses, prerequisites))
    print(solution.canFinish2(numCourses, prerequisites))

# 把列表当队列用
queue = deque(["Eric", "John", "Michael"])
# 添加
queue.append("Terry")
print(queue)
# 弹出
queue.popleft()
print("第一个到的先离开:\n{}".format(queue))
queue.popleft()
print(queue)
