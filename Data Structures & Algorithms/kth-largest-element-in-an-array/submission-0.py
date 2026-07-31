class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap =[]
        heapq.heapify(heap)
        for a in nums:
            heapq.heappush(heap, a)
            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]
        