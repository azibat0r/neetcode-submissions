"""
["1","2","+","3","*","4","-"]

comparing to what is behind it 

so save what is in the stack i am assuming must always be 2 things

[1,2]
if +
then int(stack[0]) + 
then stack pop pop
and append result of calculation to stack


["4","13","5","/","+"]

"""


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = 0
        stack = []
        for char in tokens:
            if char == "+":
                res = stack[-2] + stack[-1]
                stack.pop()
                stack.pop()
                stack.append(res)
        
            elif char == "-":
                res = stack[-2] - stack[-1]
                stack.pop()
                stack.pop()
                stack.append(res)

            elif char == "*":
                res = stack[-2] * stack[-1]
                stack.pop()
                stack.pop()
                stack.append(res)
            elif char == "/":
                res = int(stack[-2] / stack[-1])
                stack.pop()
                stack.pop()
                stack.append(res)
            else:
                stack.append(int(char))
        return stack[0]
        