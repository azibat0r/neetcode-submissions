"""

[0, 1, 2, 3, 4, 5, 6]

0.next = 6
6.next = 1
1.next = 5
5.next = 2


0,1,2
6,5,4,3

how can we identify the midpoint of the list

so l2 would jump two steps
l2.next.next

and we want it to stop when l2.next is nothing
and when it reaches that point l1 that has been taking one step would be at the midpoint
so we want that portion to be like a new list

so 0,1,2,6,5,4,3

lets make it first





"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        l1 = head
        l2 = head
        while l2 and l2.next:
            l2 = l2.next.next
            l1 = l1.next

        mid = l1.next
        l1.next = None

        prev = None
        while mid:
            store = mid.next
            mid.next = prev
            prev = mid
            mid = store

        ans = head
        while prev:
            store = ans.next
            ans.next = prev
            ans = store
            store = prev.next
            prev.next = ans
            prev = store