# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

## plan is to go down all the way left

## then go down all the way right

## process parent and switch 

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if not root:
            return

        self.invertTree(root.left)
        self.invertTree(root.right)

        temp = root.left
        root.left = root.right
        root.right = temp

        return root



        