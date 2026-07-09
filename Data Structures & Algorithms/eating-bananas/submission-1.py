class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        import math
        l = 1
        r = max(piles)
        k = r
        while l <= r:
            mid = (l + r) // 2
            hours = 0
            for a in piles:
                hours += math.ceil(a / mid)
            if hours <= h:
                k = mid
                r = mid - 1
            else:
                l = mid + 1
        return k