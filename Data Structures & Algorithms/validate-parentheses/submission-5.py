"""
"[(])"
comparing
order is important

 [
 if ] and stack[-1] == [
    pop.stack
else
    return false

"""

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == "[" or char == "{" or char == "(":
                stack.append(char)
                continue
            elif len(stack) == 0:
                return False
            elif char == "]" and stack[-1] == "[":
                stack.pop()
            elif char == "}" and stack[-1] == "{":
                stack.pop()
            elif char == ")" and stack[-1] == "(":
                stack.pop()
            else:
                return False
        if len(stack) != 0:
            return False
        return True
