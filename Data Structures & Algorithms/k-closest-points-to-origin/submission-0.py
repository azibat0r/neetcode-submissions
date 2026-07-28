class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap=[]
        heapq.heapify(heap)
        for point in points:
            x, y = point
            dist = x**2 + y**2
            heapq.heappush(heap, (-dist, point))
            if len(heap) > k:
                heapq.heappop(heap)
        output = []
        while heap:
            output.append((heapq.heappop(heap))[1])
        return output
                    

