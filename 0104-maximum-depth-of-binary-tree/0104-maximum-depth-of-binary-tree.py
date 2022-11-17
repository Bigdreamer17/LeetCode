# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
            # If check there is no root return 0
            if root == None:
                return 0
            else:
            # Else Traverse to the left and hold it in leftdepth
            # Traverse to the right and hold it in rightdepth
                leftdepth = self.maxDepth(root.left)
                rightdepth = self.maxDepth(root.right)
            # Check if  leftdepth is greater than rightdepth
                if leftdepth > rightdepth:
                # If so return the leftdepth plus 1 to account for the root Node 
                    return leftdepth + 1
                else:
                # Else return the rightdepth plus 1 to account for the root Node
                    return rightdepth + 1