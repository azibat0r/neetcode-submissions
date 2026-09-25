"""
nums = [3,4,5,6], target = 7

Input: nums = [5,5], target = 10

Output: [0,1]

3:0
4:1
5:2
6:3

for x, i in enumerate(nums):
    complement = target - x
    if target - x in dictionary:
        return [dict[c], i]
    else:
        dict[x] = i

"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i, x in enumerate(nums):
            c = target - x
            if c in hashmap:
                return [hashmap[c], i]
            else:
                hashmap[x] = i
        return []
        