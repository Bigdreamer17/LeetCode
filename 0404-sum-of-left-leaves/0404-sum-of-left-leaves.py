# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        ans = []
        def lef_sum(root, info):
            if root:
                if not root.left and not root.right and info == 'L':
                    ans.append(root.val)
                lef_sum(root.left, 'L')
                lef_sum(root.right, 'R')
        lef_sum(root, 'any')
        return sum(ans)