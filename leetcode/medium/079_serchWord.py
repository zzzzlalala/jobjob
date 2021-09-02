class solution:
    # DFS + 回溯

    def exit1(self, board, word):
        # 使用visited判断是否访问过
        visited = set()
        m = len(board)
        n = len(board[0])
        directions = [[0, 1], [0, -1], [-1, 0], [1, 0]]

        def dfs(i, j, k):
            # 结束条件
            if k == len(word) - 1:
                return word[k] == board[i][j]
            # visited记录路径
            if word[k] == board[i][j]:
                visited.add((i, j))

                for di, dj in directions:
                    if 0 <= i + di < len(board) and 0 <= j + dj < len(board[0]) and (i + di, j + dj) not in visited:
                        if dfs(i + di, j + dj, k + 1):
                            return True
                visited.remove((i, j))
            return False

        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        return False

    def exit2(self, board, word):
        m = len(board)
        n = len(board[0])
        visited = set()
        for i in range(m):
            for j in range(n):
                if self.helper(board, i, j, word, 0, visited):
                    return True
        return False

    def helper(self, board, i, j, word, k, visited):
        if k == len(word) - 1:
            return word[k] == board[i][j]
        if word[k] == board[i][j]:
            visited.add((i, j))
            for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                if 0 <= i + di < len(board) and 0 <= j + dj < len(board[0]) and (i + di, j + dj) not in visited:
                    if self.helper(board, i + di, j + dj, word, k + 1, visited):
                        return True
            visited.remove((i, j))
        return False


if __name__ == '__main__':
    test = solution()
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABCB"
    print(test.exit1(board, word))
    print(test.exit2(board, word))
