class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.list = nums        
        self.k = k
        heapq.heapify(self.list)
        while len(self.list) > k:
            heapq.heappop(self.list)

    def add(self, val: int) -> int:
        heapq.heappush(self.list, val)
        if len(self.list) > self.k:
            heapq.heappop(self.list)
        return self.list[0]
        

