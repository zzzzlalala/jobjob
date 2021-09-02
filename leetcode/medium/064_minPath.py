class solution:
    def minPathSum(self, grid):
        # 动态规划
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == j == 0:
                    continue
                # 只能横着走
                elif i == 0:
                    grid[i][j] = grid[i][j - 1] + grid[i][j]
                # 只能竖着走
                elif j == 0:
                    grid[i][j] = grid[i - 1][j] + grid[i][j]
                # 比较横着走还是竖着走小
                else:
                    grid[i][j] = min(grid[i - 1][j], grid[i][j - 1]) + grid[i][j]
        return grid[-1][-1]


if __name__ == '__main__':
    test = solution()
    grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    print(test.minPathSum(grid))
