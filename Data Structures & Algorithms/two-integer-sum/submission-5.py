"""
does the complement exist anywhere else in the array = hashmap.

orginally you wanted to build the hashmap completely then check for the complement
but,

[3,3] target = 6, causes an issue.

so
checking 3
    is 6-3 = 3 in the hashmap
        No
        Add 3:0
checking 3
    is 6-3 = 3 in the hashmap
        Yes
        Return [hashmap[3],index]

try and be efficient, don't build the hashmap in full


for i, x in enumerate(nums)
index then item
"""



class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        d = {}
        for i, x in enumerate(nums):
            search = target - x
            if search not in d:
                d[x] = i
            else:
                return [d[search], i]

        


        