# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
here we are going to make a hashmap that would store

just each node from the OG, with their values no pointers


on the second pass we would look at the OG and for each node

the copies .next should equal whatever is the OG's.next in the hashmap

so

OG
5 to  6

copy

5   6

so copy5.next = hashmap[OG5.next]
hashmap[OG5.next] and this is essentialy copy 6

so we do the same concept for random

but note
what if we have in the OG

5 to Null

Copy
5
we want copy5.next = hashmap[OG5.next]
which would be hashmap[None]
but we have not created the key for None
because our first pass stops the last node before None(no way to continue)

so when creating the hashmap we would manually add the key and values None: None



"""
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copy = {None:None}

        curr = head
        while curr:
            new = Node(curr.val)
            copy[curr] = new
            curr= curr.next

        curr = head
        while curr:
            copy[curr].next= copy[curr.next]
            copy[curr].random = copy[curr.random]
            curr = curr.next
        return copy[head] 
        
        