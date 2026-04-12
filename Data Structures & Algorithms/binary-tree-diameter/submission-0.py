# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # use the node as a connector
        # use the left subtree to form longest path
        # use the right subtree to form longest path

        # keep of track of the longest
        # recursively check for left and right subtree paths
        # also check the connector case directly against the longest
        # recursive method returns max(left, right)

        largest = 0

        def dfs(node):
            nonlocal largest
            if not node:
                return 0
            
            left_max = dfs(node.left)
            right_max = dfs(node.right)

            largest = max(largest, left_max + right_max)

            return 1 + max(left_max, right_max)

        dfs(root)

        return largest

        