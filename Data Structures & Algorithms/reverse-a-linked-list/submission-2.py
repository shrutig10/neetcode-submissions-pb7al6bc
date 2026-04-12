# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # swapping the next pointer between two nodes
        # normal way to swap, introduce a temporary value
        # introduce a temporary value
        # keep track of the previous node
        # prev, cur
        # set temp to current's next
        # set cur.next to prev
        # set prev to cur
        # set cur to temp

        cur = head
        prev = None
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        return prev
        