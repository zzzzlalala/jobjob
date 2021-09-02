from leetcode.simple.inorderTravelsal import *

class solution():
    def maxDepth(self,root):
        if root is None:
            return 0
        else:
            return max(self.maxDepth(root.left),self.maxDepth(root.right))+1


node = TreeNode(3)
node.insert(9)
node.insert(20)
node.insert(15)
node.insert(7)
test1 = solution()
print(test1.maxDepth(node))