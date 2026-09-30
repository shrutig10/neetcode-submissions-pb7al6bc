# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # keep track of the previous node and current node
        # change the next pointer
        # prev, cur
        # change cur's next to prev, set prev to cur, set cur to next
        # keep going until cur is null
        
        prev = None
        cur = head
        nxt = head.next if head else None

        while cur:
            cur.next = prev
            prev = cur
            cur = nxt
            nxt = nxt.next if nxt else None

        return prev