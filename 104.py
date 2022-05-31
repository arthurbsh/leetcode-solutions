# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def __init__(self):
        self.max = 0
    
    def solve(self, root, currentDepth):
        if root != None:
            if currentDepth > self.max:
                self.max = currentDepth
            
            self.solve(root.left, currentDepth +1)
            self.solve(root.right, currentDepth +1)
            
        
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        self.solve(root, 1)
        
        return self.max
        