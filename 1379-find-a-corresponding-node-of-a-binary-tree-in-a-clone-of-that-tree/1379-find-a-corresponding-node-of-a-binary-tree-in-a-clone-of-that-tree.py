# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def dfsinorder(o: TreeNode, c: TreeNode ):
            if o:
                dfsinorder(o.left, c.left)
                if o is target:
                    self.ans = c
                dfsinorder(o.right, c.right)
        dfsinorder(original, cloned)
        return self.ans