class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1
        r= max(piles)
        while l<r:
            mid = (l+r) //2
            counter = 0
            for a in piles:
                counter += math.ceil(a/mid)
            if counter > h:
                l= mid + 1
            elif counter <= h:
                r = mid

        return l