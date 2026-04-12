# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # bfs
        # they're stored in a queue 
        # at each iteration, take the last element in the queue
        # push all the children onto the queue
        # do not push null children!!!!
        # get the size at the beginning of each iteration
        # once we reach that number (size) push onto result

        if not root:
            return []

        res = []
        queue = deque([root])

        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                if i == size - 1:
                    res.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return res

        