# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
3 1 1

9 1 1

new node

9+3 = 12

so we need to store 2 and carry over 1 to the next nodes to calculate

2

next node = 1 + 1 + (carry over)

calculations
if ans is > 10 then store remainder and carry over should equal ans // 10

at the end if carry over is not 0 create an extra node and store answer


1 

1 1

if l2
while l2
 check if carryover is not 0 if so add it to the l2 value and create a new node for the answer

 do carryover check
 move forward


"""


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        a = l1
        b = l2
        c = ListNode()
        ans = c
        carry = 0
        while l1 and l2:
            calc = l1.val + l2.val + carry
            if calc >= 10:
                carry = calc // 10
                value = calc % 10
            else:
                value = calc % 10
                carry = 0

            new = ListNode(value)
            c.next = new
            c = c.next
            l1 = l1.next
            l2 = l2.next

        if l1:
            while l1:
                calc = carry + l1.val
                if calc >= 10:
                    carry = calc // 10
                    value = calc % 10
                else:
                    value = calc % 10
                    carry = 0

                new = ListNode(value)
                c.next = new
                c = c.next
                l1 = l1.next

        if l2:
            while l2:
                calc = carry + l2.val
                if calc >= 10:
                    carry = calc // 10
                    value = calc % 10
                else:
                    value = calc % 10
                    carry = 0

                new = ListNode(value)
                c.next = new
                c = c.next
                l2 = l2.next
        
        if carry != 0:
                value = carry
                new = ListNode(value)
                c.next = new
                c = c.next

        return ans.next
