class solution():
    # 对称二叉树
    # 递归
    def isSymmetric(self, root):
        if root == None:
            return True
        return self.dfs(root.left, root.right)

    def dfs(self, left, right):
        if left == None and right == None:
            return True
        elif left == None or right == None:
            return False
        elif left.val != right.val:
            return False
        return self.dfs(left.left, right.right) and self.dfs(left.right, right.left)
