class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.max_depth = 1

    def maxDepth(self, root: TreeNode, depth=1,) -> int:
        # What I'm thinking is that we're going to be passing the depth count as a parameter within the recursive call.
        if root is None:
            return 0

        if depth > self.max_depth:
            self.max_depth = depth

        if root.left != None:
            self.maxDepth(root.left, depth + 1)
        if root.right != None: # Note: We don't make this an else if since for each node, we want to make sure that we're also travelling on the right.
            # (if we made it an elseif, if we travelled on the left side we would never travel on the right side)
            self.maxDepth(root.right, depth + 1)
        
        return self.max_depth
    
class PracticeSolution:
    def __init__(self):
        self.max_depth = 1

    def maxDepth(self, root: TreeNode, depth=1,) -> int:
        if root is None:
            return 0
        
        if depth > self.max_depth:
            self.max_depth = depth
        
        if root.left != None:
            self.maxDepth(root.left, depth + 1)
        if root.right != None:
            self.maxDepth(root.right, depth + 1)
        
        return self.max_depth



