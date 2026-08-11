# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def swap(pt):
            if pt:
                pt.left, pt.right = pt.right, pt.left
                swap(pt.left)
                swap(pt.right)
            return

        swap(root)
        return root
        