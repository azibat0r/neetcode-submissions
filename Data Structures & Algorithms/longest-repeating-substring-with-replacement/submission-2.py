"""
AAABABB

k = 1
so you wil create a window and in each window there are characters
which can be split into the most occuring one and the others can fit into the other category ...
so we know a window is valid if the less occuring characters are less than k or equal to k
AAB , k = 1
the most occuring appears 2 times
so window length is 3
so 3 - 2 = 1, telling us that what CAN be changed is only 1 character, k allows for 1 change so the window is valid
window length is 3, meaning that the potential substring can be length 3

AABA, k = 1
window = 4
4 - 3 = 1 so window is valid

so that is what we do, and we create our window from the beginning 

AAABABB
l
r

if window is valid
r+=1

what if window is not valid,
then we move l+=1

how do we know the most frequent character in the window
as we move r
for each index we check we add it to a dictionary with the item being its frequency

then when checking if valid, we do max(hahsmap.values())

NOTE
when we move l forward
we need to decrement whatever was originally at l before we move forward

then we would have length = max(length,l-r+1), when the window is valid
and we will do so until r reaches the end of the string

"""


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = 0
        hashmap = {}
        res = 0
        for r in range(len(s)):
            if s[r] not in hashmap:
                hashmap[s[r]] = 1
            else:
                hashmap[s[r]] +=1
                
            while (r-l+1) - max(hashmap.values()) > k:
                hashmap[s[l]]-=1
                l+=1        
            
            res = max(res, r-l+1)

        return res
