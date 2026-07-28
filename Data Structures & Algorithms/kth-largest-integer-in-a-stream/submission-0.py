class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.list = nums        
        self.k = k

    def add(self, val: int) -> int:
        self.list.append(val)
        self.list = sorted(self.list)
        return self.list[-self.k]

