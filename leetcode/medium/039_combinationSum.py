from typing import List


class solution:
    # zz
    def combinationSum1(self, candidates, target):
        def dfs(candidates, start, path, ans, target):
            if target < 0:
                return
            if target == 0:
                ans.append(path)
                return
            for index in range(start, len(candidates)):
                dfs(candidates, index, path + [candidates[index]], ans, target - candidates[index])

        if len(candidates) == 0:
            return []
        path = []
        ans = []
        dfs(candidates, 0, path, ans, target)
        return ans

    # 剪枝
    def combinationSum2(self, candidates, target):
        # 回溯
        def dfs(candidates, start, path, ans, target):
            if target == 0:
                ans.append(path)
                return
            for index in range(start, len(candidates)):
                residue = target - candidates[index]
                # 小于0就不继续了(剪枝效果)
                if residue < 0:
                    return
                dfs(candidates, index, path + [candidates[index]], ans, residue)

        if len(candidates) == 0:
            return []
        candidates.sort()
        path = []
        ans = []
        dfs(candidates, 0, path, ans, target)
        return ans


if __name__ == '__main__':
    candidates = [2, 3, 5]
    target = 8
    test = solution()
    print(test.combinationSum1(candidates, target))
    print(test.combinationSum2(candidates, target))
