"""
nums = [-1,0,2,4,6,8], target = 4

so binary search but if we find mids and it is not target then it should not be considered in the range

l = mid + 1
r = mid - 1

and all of this is while l < r


"""


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1

        while l <= r:
            mid = (l + r) // 2
            check = nums[mid]
            if check == target:
                return mid
            elif check > target:
                r = mid -1
            else:
                l = mid +1

        return -1            
        