# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # iterate through each linked list (iterate together)
        # add the digits + carry (initialized to 0)
        # get the carry (1 at most) and the digit (sum % 10)
        # put the digit in the node, make the carry stay for the next iteration
        # if both lists are at the end, make a new node for carry if needed, wlse end the loop
        # while iterating, if any list reches the end, say that digit is 0
        # return the head of the new linked list

        head = cur = ListNode()
        carry = 0

        while l1 or l2 or carry:

            if not l1:
                l1_digit = 0
            else:
                l1_digit = l1.val

            if not l2:
                l2_digit = 0
            else:
                l2_digit = l2.val

            total = l1_digit + l2_digit + carry

            carry = total // 10
            digit = total % 10

            cur.next = ListNode(val=digit)
            cur = cur.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return head.next

            
            
        