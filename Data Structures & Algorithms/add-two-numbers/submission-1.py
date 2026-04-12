# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # traverse linked list
        # check that both digits exists at that space 
        # if digits, add them and store in a new node
        # if do not exist, then (if only one exists) take the number from the other list
        # if both don't exist, then done
        # if a number carries, then add one to the next iteration (carry flag)
        # create a dummy node and then return dummy.next

        dummy = cur = ListNode()
        carry = False

        while l1 or l2:

            if not l1:
                l1 = ListNode(0)
            if not l2:
                l2 = ListNode(0)

            digit = l1.val + l2.val
            if carry:
                digit += 1
                carry = False
            if digit > 9:
                carry = True
                digit %= 10
            cur.next = ListNode(digit)
            cur = cur.next
            l1 = l1.next
            l2 = l2.next

        if carry:
            cur.next = ListNode(1)

        return dummy.next



        