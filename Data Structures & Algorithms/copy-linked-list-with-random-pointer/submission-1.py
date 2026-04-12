"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # traverse the linkedlist twice
        # maintain a dictionary with the old nodes mapping to the new nodes
        # first traversal: add nodes to the dictionary (make them)
        # second traversal: adding pointers

        if not head:
            return None

        oldToNew = {}

        cur = head
        while cur:
            oldToNew[cur] = Node(cur.val)
            cur = cur.next

        cur = head
        while cur:
            new_node = oldToNew[cur]
            new_node.next = oldToNew.get(cur.next)
            new_node.random = oldToNew.get(cur.random)
            cur = cur.next

        return oldToNew[head]

        