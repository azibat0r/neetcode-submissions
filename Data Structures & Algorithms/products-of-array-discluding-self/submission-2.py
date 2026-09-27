"""
so we are going to make a left array that calculates the product of eveything to my left
a right array for product of eveything else to my right

then output would calculate the product of both numbers in the arrays at [i]

[1,2,4,6]
1  1 2  8

at 2 u do 1*1
at 4 u do 2*1
at 6 u do 4*2

[1,2,4,6]
48 24 6 1

left = [1]*len(nums)
so for i in range(1, len(nums)):
    left[i] = nums[i-1]*left[i-1]


"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1]*len(nums)
        right = [1]*len(nums)
        res = []
        for i in range(1,len(nums)):
            left[i] = nums[i-1]*left[i-1]
        for i in range(len(nums)-2,-1,-1):
            right[i] = nums[i+1]*right[i+1]
        for i in range(len(nums)):
            res.append(left[i]*right[i])
        return res

        