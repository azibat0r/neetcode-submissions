class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        store = set()
        for a in nums:
            store.add(a)
        counter = 0
        i = 0
        current = 0
        for a in nums:
            if a-1 not in store:
                current = 0
                i=0
                while a+i in store:
                    current += 1
                    i +=1
                    counter = max(counter,current)


        return counter
