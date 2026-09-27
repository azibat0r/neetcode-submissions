"""
[30,38,30,36,35,40,28]
 0   1  2  3  4  5  6

[1,4,1,2,1,0,0]

order is important
what are we saving it is index

0 
checking 38 if what is at top of the stack is less than 38, subtract index and push to res at the index of what is on the stack
then put the 38,index on stack

38
checking 30
nothing
stack = [1,2]

checking 36, it is greater than 30
so subtract index u get 1 then push 1 to res[2]
[1,3]

create a dictionary of all indexes
if what is behind me is less than me then the current,index subtract the other and append to the -1 position in output

u do this while len of stack is > 1 and what is behind me is less than me
if not continue

in the end if len of stack is > 0
for each char their index in the dictionary put 0



30,38,30,36
0,1, 2 , 3

so 
[30,38,30,36,35,40,28]

so add 30
so before adding 38 check if temp[stack[-1]] is less than me
if so then push to the res at that index the subtraction of both our indexes
and pop and append the 38
then add 30 is what is behind me less so 
add 36 does all of that

so while len(stack)>1 and what is at top is lesser than me

when not just append to the stack the index
then at the end the indexes remainnig in the stack just add [0] to them

32 31 30 40
0  1  2  3

3
[ 3  2  1    ]
"""

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        stack = []

        for i , x in enumerate(temperatures):
            while len(stack) > 0 and temperatures[stack[-1]] < x:
                res[stack[-1]] = i-stack[-1]
                stack.pop()

            stack.append(i)

        return res


        