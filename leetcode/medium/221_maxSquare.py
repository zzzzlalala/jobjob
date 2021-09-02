class solution:
    def maxSquare(self, matrix):
        rows = len(matrix)
        columns = len(matrix[0])
        if rows == 0 or columns == 0:
            return 0
        maxSide = 0
        dp = [[0] * columns for _ in range(rows)]
        for i in range(rows):
            for j in range(columns):
                if matrix[i][j] == "1":
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                    maxSide = max(maxSide, dp[i][j])
        maxSuqare = maxSide * maxSide
        return maxSuqare


if __name__ == '__main__':
    solution = solution()
    # matrix = [["1", "0", "1", "0", "0"],
    #           ["1", "0", "1", "1", "1"],
    #           ["1", "1", "1", "1", "1"],
    #           ["1", "0", "0", "1", "0"]
    #           ]
    matrix = [["0","1"]]
    print(solution.maxSquare(matrix))
