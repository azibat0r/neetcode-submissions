"""
you need to sort
basically 3 pointers, with one just incrementing and the other two do two sum
situations u need to think of
-3,-3,0,1,2
you don't want to produce -3,1,2 twice so check if the interger behind u is the same aas your current one, if so continue

now you also need to think of 
-3,0,1,2,3
if while haveing your start pointer at -3 and you do two sum on the remaining half
you will first find 0,3, but that is not the only answer, so u need to recalculate two sum by moving the b pointer +1



"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        a = 0
        nums = sorted(nums)
        res = []
        for i, x in enumerate(nums):
            b = i+1
            c = len(nums)-1
            if i > 0 and nums[i] == nums[i-1]:
                continue
            while b < c:
                target = x + nums[b] + nums[c]
                if target < 0:
                    b+=1
                elif target > 0:
                    c-=1
                else:
                    res.append([x,nums[b],nums[c]])
                    b+=1
                    while nums[b-1] == nums[b] and b < c:
                        b+=1
        return res
                    
        