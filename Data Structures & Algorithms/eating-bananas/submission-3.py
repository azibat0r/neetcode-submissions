"""
piles = [1,4,3,2], h = 9

k = 2

1,2,2,1
6

i do remember that possible answers exist in a range
from 1 to max(pile) = 4


to calculate hours for each pile is math.ceil(pile[i]/2 or k)

so you calculate the hours for a given k if hours is less than h ,
you save to max()



so now let us establish this we have our range of possible
rates 
piles = [1,4,3,2], h = 9

from 1 to 4
[1,2,3,4]
l      r

we pick the mid 
and iterate through the pile
piles = [1,4,3,2]

rate += math.ceil(pile[i]/mid)
at the end if rate <= h
then answer = min(answer,rate)

then we need to make mid smaller so 
move r to mid # we do not do mid-1, becuase that orginal position of mid is an acceptable answer

however if rate is > h 
that means the mid position is incorrect
and we will make  mid bigger
by l = mid + 1

all while l <= r
once done we will return answer

"""


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        answer = max(piles)
        while l < r:
            rate = 0
            mid = (r+l)//2
            for i in range(len(piles)):
                rate += math.ceil(piles[i]/mid)
            if rate <= h:
                r = mid
                answer = min(answer,mid)
            elif rate > h:
                l = mid + 1
        return answer


                


        