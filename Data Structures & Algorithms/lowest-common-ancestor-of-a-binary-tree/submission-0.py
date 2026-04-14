# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # at any node we can go left, right, or stay the same (return)
        # p and q can be on the same side or on either side
        # if p and q are on either side, then return this node
        # otherwise explore other options
        # we know that p and q are on opposite sides if we explore one side and cannot find a better ancestor
        # recur to find better ancestor --> go left and right and store in 2 vars
        # if both vars contain values, return this node, otherwise, return the one that is isn't null
        # base case: if cur is null, return None
        # if cur is p or q, return that node

        def dfs(cur):
            if not cur:
                return cur
            if cur.val == p.val or cur.val == q.val:
                return cur
            
            left, right = dfs(cur.left), dfs(cur.right)

            if left and right:
                return cur
            elif not left:
                return right
            else:
                return left

        return dfs(root)