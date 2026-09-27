"""

so essentially we make a list of list with [pos,speed] and sort based on position

then going from back to front we would calculate the interval then if the one on the top of the stack is greater than or equal to the one we are currently inspecting we will skip over it and continue, if the one we are inspecting is less we will add to the stack and in the end return the size of the stack

remember if it takes less time to reach the target than another it means it is faster
also if they take the time time it means they meet each other at the end
"""


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        s = set()
        c = []
        stack=[]
        for i in range(len(position)):
            c.append([position[i],speed[i]])
        c = sorted(c)
        for i in range(len(c)-1,-1,-1):
            interval = (target-c[i][0]) / c[i][1]
            if len(stack) > 0 and interval <= stack[-1]:
                continue
            else:
                stack.append(interval)
        return len(stack)

        