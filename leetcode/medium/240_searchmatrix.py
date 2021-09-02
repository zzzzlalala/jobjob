class solution:
    def searchMatrix(self, matrix, target):
        for row in matrix:
            if target in row:
                return True
        return False

    # 左下角指针
    def searchMatrix2(self, matrix, target):
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        row = len(matrix) - 1
        col = 0
        while col < len(matrix[0]) and row >= 0:
            if matrix[row][col] > target:
                row -= 1
            elif matrix[row][col] < target:
                col += 1
            else:
                return True
        return False


if __name__ == '__main__':
    solution = solution()
    matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]
    print(solution.searchMatrix(matrix, target=20))
