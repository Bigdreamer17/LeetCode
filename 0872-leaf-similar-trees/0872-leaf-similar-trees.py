# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def post(root):
            if root:
                if root.left is None and root.right is None:
                    yield root.val
                yield from post(root.left)
                yield from post(root.right)
        return list(post(root1)) == list(post(root2))