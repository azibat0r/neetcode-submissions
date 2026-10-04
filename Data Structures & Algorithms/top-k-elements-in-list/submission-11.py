"""
[1,2,2,3,3,3], k = 2

return [2,3] or [3,2]
because 3 appears 3 times
2 appears 2
1 appears once


so are going to create a hashmap
1:1
2:2
3:3

and we are going to make a [[]]
and at index 0 would be a list containing the key of the dict that has its item to be 0
and so on

what should be the length og the list of lists, the len of the nums + 1
while counter < k
then we iterate backwards
    and for each char in the list
        we append
        
when it breaks return output
"""


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        output = []
        bucket = []
        for i in range(len(nums)+1):
            bucket.append([])
        hashmap = {}
        for char in nums:
            if char in hashmap:
                hashmap[char] +=1 
            else:
                hashmap[char] = 1

        for key,item in hashmap.items():
            bucket[item].append(key)

        for i in range(len(bucket)-1,-1,-1):
            for char in bucket[i]:
                if len(output) < k:
                    output.append(char)
                else:
                    return output
        return output
                