# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def __init__(self):
        self.solution = []
    
    def solve(self, root: Optional[TreeNode]):
        if (root != None):
            self.solve(root.left)
            self.solution.append(root.val)
            self.solve(root.right)
    
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        self.solve(root)
        
        return self.solution
        