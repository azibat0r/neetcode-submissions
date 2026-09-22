"""
so we want to iterate through it once
[1,2,4,6]

right = [2,4,6]
product = 48
left = []
at [0] = 48 * nothing

at [1]
left = [1]
right = [4,6] which was 48 / nums[1] * left

i think i need a pointer
a = 0
right = nums[1:len(nums)]
right = [2,4,6] or [48]

u had the right idea of 2 arrays
so

prefix [1,1,2,8]
suffix [48,24,6,1]

building prefix
for i in range(nums)
if i == 0
append.1
total = 1
else
total *= nums[i-1]

building suffix
result = [0] * len(num)
for i in range(len(nums)-1,0,-1)
if i == len(nums)-1
append[i] = 1
total = 1
else
total *= nums[i-1]

"""


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        suffix = [0]*len(nums)
        total = 1
        for i in range(len(nums)):
            if i == 0:
                prefix.append(1)
            else:
                total *= nums[i-1]
                prefix.append(total)
        total = 1
        for i in range(len(nums)-1,-1,-1):
            if i == len(nums)-1:
                suffix[i] = 1
            else:
                total *= nums[i+1]
                suffix[i] = total

        result = []
        for i in range(len(nums)):
            result.append(suffix[i]*prefix[i])
        return result                


        