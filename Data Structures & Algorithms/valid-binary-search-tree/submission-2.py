# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        # helper method, recursive one --> check for valid bst with an interval
        # if the node does not exist, return true
        # check that the node's value falls within the interval
        # if falls within the interval --> check children
        # left child --> adjust interval so that upper bound is current node's value
        # right child --> adjust intercal so that lower bound is current node's value

        # outer isValidBST, simply call the helper with left and right children and set their intervals


        return self.validBSTHelper(root, float('-inf'), float('inf'))

    def validBSTHelper(self, root, lower, upper) -> bool:
        if not root:
            return True
        
        if root.val <= lower or root.val >= upper:
            return False
        
        return self.validBSTHelper(root.left, lower, root.val) and self.validBSTHelper(root.right, root.val, upper)
        
        