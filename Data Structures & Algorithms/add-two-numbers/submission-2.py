# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # sum of the digits as well as the carry
        # adding a new node at the end of the linked list
        # while we have a node in either list or we have a value to carry over
        # add the digits of the two linked lists together + carry 
        # value that will be stored == sum % 10
        # carry = sum // 10
        # move forward on both linked lists
        # if either linked list contains is none, just set it to 0

        head = cur = ListNode()
        carry = 0

        while l1 or l2 or carry:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0

            total = l1_val + l2_val + carry
            digit = total % 10
            carry = total // 10

            cur.next = ListNode(digit)

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
            cur = cur.next

        return head.next