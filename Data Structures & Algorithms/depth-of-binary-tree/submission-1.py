# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # start count at 0
        # try to go to children
        # if neither child exist, simply return
        # take the maximum depth from either child
        # base case --> root is null, return 0

        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
        