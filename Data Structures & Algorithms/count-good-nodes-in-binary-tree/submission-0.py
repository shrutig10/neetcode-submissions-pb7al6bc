# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # root will always be good
        # post order
        # want to see whether this node is good or not
        # we check its children after updating maximum in path
        # keep track of the minimum value in that path
        # dfs - send in node and current max of that path
        # if this node's value is <= max, then increment good counter
        # otherwise update maximum for this path
        # check children

        res = 0

        def dfs(node, max_val):
            nonlocal res

            if not node:
                return
            if node.val >= max_val:
                res += 1
                max_val = max(node.val, max_val)

            dfs(node.left, max_val)
            dfs(node.right, max_val)

        dfs(root, root.val)
        return res

        