class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        l = []
        
        for s in stones:
            l.append(-s)
        heapq.heapify(l)
        while len(l) > 1:
            x = heapq.heappop(l)
            y = heapq.heappop(l)
            if x == y:
                pass
            else:
                heapq.heappush(l, -abs(x-y))
        if len(l) == 1:
            return -l[0]
        else:
            return 0
        
