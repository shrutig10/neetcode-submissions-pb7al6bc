# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # base case: go through the tree until you find a node that is either between them, or equal to one of them
        # if node is smaller than both, go to the right
        # if node is greater than both, go to the left
        # dfs

        def dfs(cur):
            if cur.val == p.val or cur.val == q.val or (cur.val < p.val and cur.val > q.val) or (cur.val > p.val and cur.val < q.val):
                return cur
            elif cur.val < p.val:
                return dfs(cur.right)
            else:
                return dfs(cur.left)
        
        return dfs(root)