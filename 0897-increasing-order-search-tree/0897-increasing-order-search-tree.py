# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        ans = []
        def dfs(root):
            if root:
                yield from dfs(root.left)
                
                yield root.val
                
                yield from dfs(root.right)
        ans = cur = TreeNode(None)
        for i in dfs(root):
            cur.right = TreeNode(i)
            cur = cur.right
        return ans.right