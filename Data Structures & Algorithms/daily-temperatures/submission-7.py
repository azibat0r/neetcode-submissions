"""
so store current on the stack

[30,38,30,36,35,40,28]
 0  1  2  3  4  5  6
so store index on the stack


[0] compare 38 to 30  so we would append 1 - 0
then pop
push 38 to stack
[1] compare 30  less than
push 30
[1,2] compare 36
pop and append 3 - 2 at the position of the pop
compare 36 to 38
push 36
[1,3,4] compare 40
append 1 at position 4
append 2 at posiion 3
append 4 at position 1

so all of this happend for each character in temperature
then we go through the stack again and put 0 in the other positions remaining




"""

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        result = [0] * len(temperatures)
        stack = []

        for i, n in enumerate(temperatures):
            if stack:
                while stack and n > temperatures[stack[-1]]:
                    result[stack[-1]] = i - stack[-1]
                    stack.pop()
                stack.append(i)
            else:
                stack.append(i)

        return result
        