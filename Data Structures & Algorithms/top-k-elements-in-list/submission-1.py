class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        store = {}
        for a in nums:
            store[a]= 1 + store.get(a,0)

        result = []
        for b,c in store.items():
            result.append([c,b])
        result.sort()

        final=[]
        for i in range(k):
            final.append(result.pop()[1])
        return final
                

        