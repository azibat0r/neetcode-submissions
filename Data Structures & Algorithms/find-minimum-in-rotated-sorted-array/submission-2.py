class Solution:
    def findMin(self, nums: List[int]) -> int:
        """ there is a good interval and bad inteval. good = 1,2,3,4 bad = 3,4,1,2
good is if l < r and bad is if l > r
when good, l is minimum

so we are going to check if we first have a good interval, if not we need to check whether the
fall is on the left or right of the midpoint
0,1,2,3,4
3,4,5,1,2 
lenght is 5 (4)
midpoint is 2 = 5
3 < 5 > 2
so we save 5
and check right of 5 """

        l = 0
        r = len(nums) - 1
        res = nums[0]
        while l <= r:
            mid = (l+r)//2
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            
            elif nums[mid] >= nums[l]:
                res = min(res, nums[mid])

                l = mid + 1
            else:
                res = min(res, nums[mid])
                r = mid -1
        return res


