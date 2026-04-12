# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # first element of preorder is always the root node
        # position in inorder matches subtree location
        # continue splitting the inorder array based off of which element we are looking at in preorder

        # iterate through preorder <-- outside of the recursion
        # find the index of it in inorder <-- use a hashmap
        # recursively create the subtrees with the subarrays

        locations = {}
        for i in range(len(inorder)):
            locations[inorder[i]] = i

        pre_idx = 0

        def dfs(l, r):
            nonlocal pre_idx
            if l > r:
                return None
            root = TreeNode(preorder[pre_idx])
            pivot = locations[preorder[pre_idx]]
            pre_idx += 1
            root.left = dfs(l, pivot - 1)
            root.right = dfs(pivot + 1, r)

            return root

        return dfs(0, len(inorder) - 1)





        