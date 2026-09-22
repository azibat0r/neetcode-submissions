"""
Input: nums = [1,2,2,3,3,3], k = 2

Output: [2,3]

looking at frequency

1:1
2:2
3:3

7:2
[,,7]
1:2
2:2
[[],[],[1,2]]

[,1,2,3]

build a hashmap holding frequency

build a list
where index represents amount appeared
and item is a list containing numbers that have a frequency == index

building the list
it should hold lists of max amount length of nums
    for i in range(len(nums)):
        l.append([])
for key, item in hashmap.items():
    l[item].append(key)

counter = 0
going backwards
    while counter != k
    for char in l[i]
        result.append(char)
        counter+=1

"""


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        l = []
        for i in range(len(nums)+1):
            l.append([])

        hashmap = {}
        for i in range(len(nums)):
            if nums[i] not in hashmap:
                hashmap[nums[i]] = 1
            else:
                hashmap[nums[i]] += 1
        for key, item in hashmap.items():
            l[item].append(key)
        counter = 0
        result = []
        for i in range(len(l)-1,-1,-1):
            for char in l[i]:
                if len(l[i]) == 0:
                    continue
                elif counter == k:
                    return result
                else:
                    result.append(char)
                    counter+=1

        return result

        
