class solution:
    def dfs(self, grid, r, c):
        grid[r][c] = 0
        dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        for x, y in dir:
            x = r + x
            y = c + y
            if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == "1":
                self.dfs(grid, x, y)

    def numIsland(self, grid):
        if len(grid) == 0:
            return 0
        numIsland = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    numIsland += 1
                    self.dfs(grid, r, c)
        return numIsland


if __name__ == '__main__':
    solution = solution()
    grid1 = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    grid2 = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]

    print(solution.numIsland(grid1))
    print(solution.numIsland(grid2))
