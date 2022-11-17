# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Createing a list to hold our answer
        ans = []
        #Our fucntion the traverses in-order
        def inorder(root):
            # Checking if we have a root 
            if root:
                # First traverseing to the left 
                inorder(root.left)
                # Then adding our Node(root) value to ans 
                ans.append(root.val)
                # finally traverseing to the right
                inorder(root.right)
        
        inorder(root)
        return ans
            