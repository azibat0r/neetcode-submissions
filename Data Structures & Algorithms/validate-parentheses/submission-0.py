class Solution:
    def isValid(self, s: str) -> bool:
        if ((len(s) % 2) != 0):
            return False
        pairs = {')':'(', '}':'{',']':'['}
        stack=[]
        for k in s:
            if k in pairs:
                if stack and stack[-1] == pairs[k]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(k)
        return len(stack) == 0

        