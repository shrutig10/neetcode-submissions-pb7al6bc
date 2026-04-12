# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # start a new path from that node and try both sides (as a connector between l and r subtrees)
        # stop the path there (take it and not try any children)
        # take the node as part of the sum, and then try left or right

        # dfs
        # post order traversal --> calculate the max of the subtrees and then pick the best sum from there

        # have a maximum length
        # run dfs on root
        # try both subtrees (and get max sum from both of them)
        # if one subtree is larger than the other and is not already using the connecting sum, just use that subtree
        # compare with cur_sum + node and take max and compare with stored maximum

        largest = root.val

        def dfs(node):
            nonlocal largest
            if not node:
                return 0
            
            left_max = max(0, dfs(node.left))
            right_max = max(0, dfs(node.right))
            largest = max(largest, node.val + left_max + right_max)

            return node.val + max(left_max, right_max)

        dfs(root)
        return largest



        