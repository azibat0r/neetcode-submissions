class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in range(len(tokens)):
            stack.append(tokens[i])
            if (tokens[i] == "+"):
                stack.pop()
                b = int(stack.pop())
                a = int(stack.pop())
                stack.append(a+b)
            elif (tokens[i] == "-"):
                stack.pop()
                b = int(stack.pop())
                a = int(stack.pop())
                stack.append(a-b)
            elif (tokens[i] == "*"):
                stack.pop()
                b = int(stack.pop())
                a = int(stack.pop())
                stack.append(a*b)
            elif (tokens[i] == "/"):
                stack.pop()
                b = int(stack.pop())
                a = int(stack.pop())
                stack.append(int(a/b))
            else:
                continue
        return int(stack[-1])
