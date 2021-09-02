class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class solution:
    def mergeTree(self, root1, root2):
        if not root1: return root2
        if not root2: return root1
        merged = TreeNode(root1.val + root2.val)
        merged.left = self.mergedTree(root1.left, root2.left)
        merged.right = self.mergedTree(root1.right, root2.right)
        return merged
