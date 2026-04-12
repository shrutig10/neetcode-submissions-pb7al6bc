# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # dfs
        # post order traversal
        # get height of left subtree 
        # get height of right subtree
        # check that they are within 1
        # return that

        is_balanced = True

        def dfs(node, height):
            nonlocal is_balanced
            if not node:
                return 0
            left_height = dfs(node.left, height)
            right_height = dfs(node.right, height)
            if abs(left_height - right_height) > 1:
                is_balanced = False
            return 1 + max(left_height, right_height)

        dfs(root, 0)
        return is_balanced
        