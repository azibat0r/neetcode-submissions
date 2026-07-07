class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1] * len(nums)
        for i in range(1, len(nums)):
            left[i] = nums[i-1] * left[i-1]
        right = [1] * len(nums)  #to fill up the last one with 1 
        for i in range(len(nums)-2, -1, -1): #reread this
            right[i] = nums[i+1] * right[i+1]

        result=[]
        for i in range(len(nums)):
            result.append(right[i] * left[i])
        return result



