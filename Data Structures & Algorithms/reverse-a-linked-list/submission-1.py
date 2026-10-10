# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



"""
c = head is how you create a pointer to a node
p = None is valid

head is just a pointer to the first thing in the node
not the whole node 

Nothing   0    1
               0.next
prev      cur

we want 0.next to point to where prev is
but it severs the connection to 1
so we need to store 1 somewhere

Nothing   0    1
               0.next
prev      cur   store

then, cur.next = prec

Nothing   0    1
0.next
prev      cur   store

then we want all to move forward,
dont make cur forward first cause u loose connection to 0

prev = cur
then
cur = store

all of this happens while there is a current node that exists

also at the end of a node, the last elements.next is = to None




"""
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        prev = None

        while current:
            store = current.next
            current.next = prev
            prev = current
            current = store
        
        return prev

            

            

        
