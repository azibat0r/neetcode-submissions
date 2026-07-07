class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        pairs = []
        for i in range(len(position)):
            pairs.append((position[i], speed[i]))
        pairs = sorted(pairs)
        for i in range(len(position)-1,-1,-1):
            d = (target - pairs[i][0])/ pairs[i][1]
            if not stack:
                stack.append(d)
            elif (d > stack[-1]):
                stack.append(d)
        return len(stack)