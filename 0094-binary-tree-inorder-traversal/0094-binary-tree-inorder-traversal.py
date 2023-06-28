# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:


        result = []

        def inorder(root):
            if not root: #base case if tree empty then return empty
                return
            else:
                inorder(root.left) #traverse on left first in in order
                result.append(root.val)
                inorder(root.right)

        inorder(root)   #recursive call
        return result