# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # check nodes in root and see if children match
        # if subroot is null --> it is a subtree
        # if root is null --> can't have a subtree
        # if neither are null
            # check values --> if not equal, not a subtree, equal --> check children
        # check every node in root for being a subtree

        if not subRoot:
            return True
        if not root:
            return False

        return self.isSame(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSame(self, root, subRoot) -> bool:
        if not subRoot and not root:
            return True
        if not subRoot or not root:
            return False

        if root.val == subRoot.val:
            return self.isSame(root.left, subRoot.left) and self.isSame(root.right, subRoot.right)
        else:
            return False

