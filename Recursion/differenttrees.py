from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Chatgpt generated, theres no understanding this shit 
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        # Starting from the root node, we must consider every possibility for which 
        if n == 0:
            return []
        
        def build(start, end):
            if start > end:
                return [None]
        
            all_trees = []

            for root_val in range(start, end + 1):
                for left in build(start, root_val - 1):
                    for right in build(root_val + 1, end):
                        all_trees.append(TreeNode(root_val, left, right))
            
            return all_trees

        return build(1, n)