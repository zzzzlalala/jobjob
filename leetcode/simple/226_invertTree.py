class solution:
    def invertTree(self,root):
        if root is not None:
            root.left,root.right = self.invertTree(root.right),self.invertTree(root.left)
        return root