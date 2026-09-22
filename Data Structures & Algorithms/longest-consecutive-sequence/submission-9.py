"""

[2,3,4,5,7,8,9,10,11]

4

2:3
3:4
4:5
5:6
7:8
9:10
11:12

0:1
1:2
1:2
2:3
3:4
4:5
5:6
6:7

counter = 1
res= -1
for key, item in d.items()
    if item in key:
        counter +=1
    current = counter  4
    counter = 0
    res = max(res,current)

"""


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d = {}

        for char in nums:
            if char in d:
                pass
            else:
                d[char] = char+1
        
        counter = 0
        res = 0
        for key, item in d.items():
            if key-1 not in d:
                current = key
                counter +=1
                while d[current] in d:
                    current = d[current]
                    counter+=1
                length = counter
                counter = 0
                res = max(res,length)
            else:
                pass

        return res



        