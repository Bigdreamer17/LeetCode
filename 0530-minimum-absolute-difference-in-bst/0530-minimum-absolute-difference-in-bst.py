# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    temp = -float('inf')
    ans = float('inf')
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        if root.left:
            self.getMinimumDifference(root.left)
        self.ans = min(self.ans, abs(root.val - self.temp))
        self.temp = root.val
        if root.right:
            self.getMinimumDifference(root.right)
        return self.ans