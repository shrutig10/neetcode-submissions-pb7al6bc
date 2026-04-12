# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # num rotations = k % len(linked list)
        # iterate through list to get the total length
        # keep a pointer at the tail
        # iterate as many times as there are rotations
        # keep a pointer to the current node's next
        # set tail's next to head
        # set cur pointer's next to None
        # set the head to the cur node's next (stored earlier)

        if not head or k == 0:
            return head

        length = 0
        cur = head

        while cur:
            length += 1
            if not cur.next:
                tail = cur
            cur = cur.next
        
        rotations = k % length
        if rotations == 0 or length == 1:
            return head

        cur = head
        for _ in range(length - rotations - 1):
            cur = cur.next
        
        temp = cur.next
        tail.next = head
        cur.next = None
        head = temp

        return head


        



        