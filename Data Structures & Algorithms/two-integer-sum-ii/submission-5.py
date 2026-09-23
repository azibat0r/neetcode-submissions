"""

sorted
you need to compare 2 things, add together


Input: numbers = [1,2,3,4,7], target = 6

2+1 = 3
3+2 = 5
4+3 = 7
4+1 =
7+1 = 8
4+1
"""


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        a = 0
        b = len(numbers)-1
        calc = numbers[a] + numbers[b]
        while (numbers[a] + numbers[b]) != target:
            calc = numbers[a] + numbers[b]
            if calc > target:
                b-=1
            else:
                a+=1
        return [a+1,b+1]

            

        