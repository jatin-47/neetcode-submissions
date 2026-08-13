# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def maxdep(root):
            if not root:
                return 0
            ht = 1
            ht += max(maxdep(root.left), maxdep(root.right))
            return ht
        return maxdep(root)
        