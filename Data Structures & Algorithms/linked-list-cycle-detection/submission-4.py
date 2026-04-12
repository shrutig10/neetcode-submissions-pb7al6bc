# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # loop through the list
        # keep track of nodes that have been visited
        # on next iteration, if we visit a node that has been visited, return True
        # visited will be a set

        visited = set()

        while head:
            if head in visited:
                return True
            visited.add(head)
            head = head.next
        
        return False
        