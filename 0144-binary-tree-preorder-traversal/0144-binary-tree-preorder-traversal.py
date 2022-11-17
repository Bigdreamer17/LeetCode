# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Pre-order aka n, l, r 
        ans = []
        def pre(root):
            if root:
                # Adding the value of our node 
                ans.append(root.val)
                # Then moving to the right side of tree
                pre(root.left)
                # Finally moving to the right side
                pre(root.right)
        pre(root)
        return ans