# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # run a breadth first search
        # making sure that children of a certain level are all added
        # normal bfs - use a queue; while queue
        # base case - if root is null, return empty list
        # make a queue and add root to it
        # while loop --> while queue
        # for loop --> get current size and pop that many times
        # add values to result
        # add children to queue

        if not root:
            return []

        res = []
        q = deque([root])

        while q:
            cur_size = len(q)
            cur_entry = []
            for i in range(cur_size):
                cur_node = q.popleft()
                cur_entry.append(cur_node.val)
                if cur_node.left:
                    q.append(cur_node.left)
                if cur_node.right:
                    q.append(cur_node.right)
            res.append(cur_entry)

        return res


        