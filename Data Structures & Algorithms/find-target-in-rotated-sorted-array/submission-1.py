"""

[3,5,6,0,1,2] target is 2

so in this question we are looking for
the sorted path
and from the info in the sorted path we can deduce whether to move forward or not

so we have 3  6   2
so our mid is 6
and we check if mid is equal to target
the sorted path is 3 5 6
now our target it should be between this path
that is 3 < target < 6
if it is not that means it exists on the
right side



so we have different cases the

find mid
CHECK if mid = target
then find valid path
if target not COMPLETELY in path

"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums)-1

        while l <= r:
            mid = (r+l)//2
            if target == nums[mid]:
                return mid
            
            if nums[mid] >= nums[l]:
                if target < nums[l] or target > nums[mid]:
                    l = mid+1
                else:
                    r = mid - 1
            elif nums[mid] <= nums[r]:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid+1

        return -1






