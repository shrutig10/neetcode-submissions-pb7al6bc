# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # carry value
        # go backwards 
        # using a stack --> also helps with place values
        # create a l1 stack and create l2 stack
        # push all the values of each list onto their respective stack
        # while either stack has an element or we have a carry value
        # create a node with the digit (stack1 + stack2 + carry) % 10
        # carry = sum // 10
        # set the node's next to the head and then set the head to the node
        # if our lists are unequal lengths, if we encounter a stack with empty elements --> add 0 for that


        stack1, stack2 = [], []
        head = None

        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        
        while l2:
            stack2.append(l2.val)
            l2 = l2.next

        carry = 0

        while stack1 or stack2 or carry:
            l1_val = stack1.pop() if stack1 else 0
            l2_val = stack2.pop() if stack2 else 0

            total = l1_val + l2_val + carry
            digit = total % 10
            carry = total // 10

            cur = ListNode(digit)
            cur.next = head
            head = cur

        return head

        # []
        # []
        # l1_val = 0, l2_val = 8, carry = 0
        # total = 9, digit = 9
        # cur = 9 --> 9 --> 6 --> None










