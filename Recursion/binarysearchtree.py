class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root == None: # If when traversing the binary search tree we read the end (i.e. the root.left or root.right returns None), then the value we're looking for doesn't exist.
            return None
        
        if val == root.val:
            return root
        
        if val < root.val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)