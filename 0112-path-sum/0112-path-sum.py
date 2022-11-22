# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def helper(root, total):
            if not root:
                return
            elif not root.left and not root.right:
                if total + root.val == targetSum:
                    return True 
            else:
                return helper(root.left, total + root.val) or helper(root.right, total + root.val)
        if root:
            return helper(root, 0)