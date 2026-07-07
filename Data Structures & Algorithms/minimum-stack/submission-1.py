class MinStack:

    def __init__(self):
        self.s = []
        self.minimum = []

    def push(self, val: int) -> None:
        self.s.append(val)
        if self.minimum:
            smallest = min (val, self.minimum[-1])
            self.minimum.append(smallest)
        else:
            self.minimum.append(val)

        
    def pop(self) -> None:
        self.s.pop()
        self.minimum.pop()

    def top(self) -> int:
        return self.s[len(self.s)-1]
        

    def getMin(self) -> int:
        return self.minimum[-1]
        
