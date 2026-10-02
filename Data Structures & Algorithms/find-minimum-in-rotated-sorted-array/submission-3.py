"""
so your intutition was correct however
what we need to do is remember that it was sorted 
[3,4,5,6,1,2]

we can identify the sorted portion by comparing to the endpoints
so 5 is our mid
3  5  2
so 3 to 5 is normal
5 to 2 this tells me the drop occurs in this region
now since 5 is greater than 2 it cannot be the minumum
so we do l = mid+1

[4,5,0,1,2,3]
we have 

4  0  3
so since 0 is less than 4
now it means 0 could still possibly be the answer
so we do r = mid

and because of the r = mid our while loop has to be l < r

"""


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        while l < r:
            mid = (l+r)//2
            if nums[mid] <= nums[r]:
                r = mid
            elif nums[0] <= nums[mid]:
                l = mid+1
        return nums[l]


        