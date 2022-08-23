class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root: # Base case, return 0 if tree is empty.
            return 0
        
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1 # Else return the maximum value of left or right subtree plus 1.

'''
Time: O(n)
Space: O(n)
'''
