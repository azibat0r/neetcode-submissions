"""

Base case

for nums in whaterever
constraint
continue

action
call function
undo



how do i know its backtracking
all possible combinations

what is the base case
if what is being added up to > target

what we need to track
a current sum
a current path array
main restult array

so for a in nums

2
sum += 2 
call again
2
sum = 4
call again
until 10
2
call
check
10
check
fail
8



1. 3 [3]
check
2.6 [3,3]
check
3. 9 [3,3,3]
4. 12 [3,3,3,3]
5. 15 [3,3,3,3,3]
check
6. 18 [3,3,3,3,3,3]
check
return to 6.
6.  15 [3,3,3,3,3]
return to 5, where num was 3

"""


class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        path = []
        count = 0
        def backtracking(start, count, path):
            if count == target:
                result.append(path[:])
                return
            if count > target:
                return
            for i in range(start, len(nums)):
                num = nums[i]
                if count + num > target:
                    continue
                count += num
                path.append(num)
                backtracking(i, count, path)
                path.pop()
                count -= num
        backtracking(0, count, path)
        return result


