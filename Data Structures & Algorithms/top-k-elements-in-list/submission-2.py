"""
Frequency
nums = [1,2,2,3,3,3], k = 2
return the 2 most frequent element
1:1
2:2
3:3

O(n)

What is important
The frequency of the element, not order
Hashmap
1:1
2:2
3:3

How do we pick the top 2
we have a return list []
is there a way to find the key of a dict, when you know the value

so what is imporant 
we need to know the frequency of each number
and sort based on said frequency

a list containing lists
where index represents frequency
and inner list represents number that has that frequency

so we create the hashmap
and create a list of list
that is like the inverse of the hashmap
then we input the respective numbers at their frequencies
the length of the list of list is the length of nums + 1
because with a list
0,1,2,3,4,5,6
from nums = [1,1,1,1,1,1]
the maximum possible frequency is  6 so we need to accomadate for it

then going from 6 to 0 we add whaterver number is in the list to the result list
then when lenght of result list = k we return result list

"""


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []

        hashmap = {}
        for x in nums:
            if x not in hashmap:
                hashmap[x] = 1
            else:
                hashmap[x] += 1
        
        bucket = []
        for i in range(len(nums)+1):
            bucket.append([])
        
        for key, item in hashmap.items():
            bucket[item].append(key)
        for i in range(len(bucket)-1,0,-1):
            for x in bucket[i]:
                result.append(x)
                print(result)
                if len(result) == k:
                    return result
        