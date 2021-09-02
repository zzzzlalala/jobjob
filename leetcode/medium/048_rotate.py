class solution:
    def rotate1(self, matrix):
        # 第i行j列 到 倒数第i列第j个位置
        n = len(matrix)
        matrix_new = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                matrix_new[j][n - i - 1] = matrix[i][j]
        matrix[:] = matrix_new
        return matrix

    def rotate2(self, matrix):
        # 翻转替代旋转
        # 水平轴 matrix[row][col] = matrix[n-row-1][col]
        # 主对角线 matrix[row][col] = matrix[col][row]
        n = len(matrix)
        for i in range(n // 2):  # 上半区反转
            for j in range(n):
                matrix[i][j], matrix[n - i - 1][j] = matrix[n - i - 1][j], matrix[i][j]
        for i in range(n):
            for j in range(i): # 对角线左侧反转
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        return matrix



if __name__ == '__main__':
    test = solution()
    matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(test.rotate1(matrix1))
    print(test.rotate2(matrix))
