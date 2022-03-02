def inorderTraversal(self, A):        
    return [] if not A else  self.inorderTraversal(A.left) +[A.val] + self.inorderTraversal(A.right)
def kthSmallest(self, A, k):        
    l = []
    l = self.inorderTraversal(A)
    return l[k-1]
