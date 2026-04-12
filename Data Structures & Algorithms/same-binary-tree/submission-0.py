# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # iterate through each node
        # if they are the same value, then try children
        # if not the same value, return False
        # return True when we've gone through the entire tree, and no values are different
        # base case: if both are null, return True
        # if either is null, return False
        # check values

        if not p and not q:
            return True
        elif not p or not q:
            return False
        elif p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        