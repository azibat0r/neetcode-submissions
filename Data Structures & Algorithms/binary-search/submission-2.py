"""
so listen
in binary search whatever is included from l to r that is counting l and r
is valid for the check
but when we find out mid is not equal to target
and we want to update l and r, mid should not be in that new window
so l = mid and r = mid is wrong

also to calculate mid is (l+r)//2
also the while loop should be l <=r
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
 
        while l<=r:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return -1
        