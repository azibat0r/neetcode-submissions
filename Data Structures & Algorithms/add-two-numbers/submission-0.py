# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a = l1
        b = l2
        l3 = ListNode()
        c = l3
        carry = 0
        while a or b or carry:
            if a:
                a_val = a.val
                a = a.next
            else:
                a_val = 0

            if b:
                b_val = b.val
                b = b.next
            else:
                b_val = 0

            total = a_val + b_val + carry
            carry = total // 10
            digit = total % 10

            c.next = ListNode(digit)   # create new node
            c = c.next      
        return l3.next

                   
            




