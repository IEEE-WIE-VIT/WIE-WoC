def preorderTraversal(self, A):
        return [] if not A else [A.val] + self.preorderTraversal(A.left) + self.preorderTraversal(A.right)
            
