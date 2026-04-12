# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        # perform a breadth first search
        # append that value along with a ;/space/some kind of marker to our string
        # if no child, then write null/none/something else to the string

        queue = deque()
        res = ''

        queue.append(root)
        while queue:
            node = queue.popleft()
            if not node:
                res += 'N;'
                continue
            res += str(node.val) + ';'
            queue.append(node.left)
            queue.append(node.right)

        return res if root else 'N;'

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        # split the string based off the delimeter
        # perform a bfs to build the tree

        queue = deque()
        list_data = data.split(';')[:-1]
        if list_data[0] == 'N':
            return None

        idx = 0
        root = TreeNode(int(list_data[idx]))
        queue.append(root)
        idx += 1

        while queue:
            node = queue.popleft()
            if list_data[idx] != 'N':
                node.left = TreeNode(int(list_data[idx]))
                queue.append(node.left)
            idx += 1
            if list_data[idx] != 'N':
                node.right = TreeNode(int(list_data[idx]))
                queue.append(node.right)
            idx += 1

        return root


