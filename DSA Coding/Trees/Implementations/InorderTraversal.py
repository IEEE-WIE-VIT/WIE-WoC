def inorderTraversal(self, A):
        return [] if not A else  self.inorderTraversal(A.left) +[A.val] + self.inorderTraversal(A.right)
