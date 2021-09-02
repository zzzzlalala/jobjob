class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def insert(self, val):
        # 小的放左边大的放右边，空的新建节点，否则向下递归查找
        if self.val:
            if val < self.val:
                if self.left is None:
                    self.left = TreeNode(val)
                else:
                    self.left.insert(val)
            elif val > self.val:
                if self.right is None:
                    self.right = TreeNode(val)
                else:
                    self.right.insert(val)

        else:
            self.val = val

    def PrintTree(self):
        '''
        前序：打印，左，右
        中序：左，打印，右
        后序：左，右，打印
        :return:
        '''
        # 中序打印
        if self.left:
            self.left.PrintTree()
        print(self.val)
        if self.right:
            self.right.PrintTree()


class solution:
    # 中序遍历
    # 递归
    def inorderTraversal(self, root):
        list = []

        def zhongxu(root):
            if not root:
                return
            else:
                zhongxu(root.left)
                list.append(root.val)
                zhongxu(root.right)
            zhongxu(root)
            return list
    # 迭代
    def inorderTraversal1(self,root):
        stack,res = [root],[]
        while stack:
            i = stack.pop()
            if isinstance(i,TreeNode):
                stack.extend([i.right,i.val,i.left])
            elif isinstance(i,int):
                res.append(i)
        return res



if __name__ == '__main__':
    node = TreeNode(12)
    node.insert(6)
    node.insert(14)
    node.insert(3)

    node.PrintTree()

    test = solution()
    test.inorderTraversal(node)
    test.isSymmetric(node)
