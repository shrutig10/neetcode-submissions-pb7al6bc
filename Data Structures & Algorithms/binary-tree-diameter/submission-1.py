# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # recursion --> dfs
        # options at a node: go down left, go down the right, go down both
        # only go down both once
        # running max
        # check left and right in recursive method
        # check the max with the both path (max of the left + max of the right)
        # return 1 + max left, right
        # base case: if not node, return 0

        result = 0

        def dfs(node):
            nonlocal result

            if not node:
                return 0
            left_max = dfs(node.left)
            right_max = dfs(node.right)
            result = max(result, left_max + right_max)
            return 1 + max(left_max, right_max)

        dfs(root)
        return result
        