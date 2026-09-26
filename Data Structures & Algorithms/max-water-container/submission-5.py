"""
pick 2
the smallest determines the height

1,7,2,5,4,7,3,6

0,1,2,3,4,5,6,7

so picking 1 and 6
area is min between pointer x index of r-index of l ans = 7*1
now since min determines the area that is the one we should move
so we then move l to 7
lets try that with another example

[2,2,2]
l     r

so area =

2 pointers
area = min between pointers * my subtraction of index
then we save the max and return at the end
so while l < r
calc area 
if l < r
l+= 1
else
r-=1
"""

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1
        res = 0
        while l < r:
            smaller = min(heights[l],heights[r])
            calc = smaller * (r-l)
            res = max(res,calc)
            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1
        return res
        