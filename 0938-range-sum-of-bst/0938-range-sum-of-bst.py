# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
def printLevelOrder(root):
    Check value node.val and if it is in our range, add it to global sum.
We need to visit left subtree only if node.val > low, that is if node.val < low, it means, that all nodes in left subtree less than node.val, that is less than low as well.
Similarly, we visit right subtree only if node.val < high.

"""
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(root):
            if root == None:
                return
            if low <= root.val <= high:
                self.ans += root.val
            if root.val > low:
                dfs(root.left)
            if root.val < high:
                dfs(root.right)
                
        self.ans = 0
        dfs(root)
        return self.ans