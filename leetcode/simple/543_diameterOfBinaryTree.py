# 深度优先搜索
# 二叉树的直径=该路径经过的节点数减1
# 两个叶子节点的路径= 根节点左右儿子的深度之和
class solution:
    def diameterOfBinaryTree(self, root):
        def depth(root):
            if not root: return 0
            L = depth(root.left)
            R = depth(root.right)
            #  最大节点数全局变量ans记录node最大的值
            ans = max(self.ans, L + R+1)
            # 返回该节点为根的子树的深度
            return max(L, R) + 1

        depth(root)
        return self.ans-1
