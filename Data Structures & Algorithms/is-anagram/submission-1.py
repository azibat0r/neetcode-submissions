class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
    #    hashmap = dict()
        hashmapA = {}
        hashmapB = {}
        listA = []
        listB = []
        s = ''.join(sorted(s))
        t = ''.join(sorted(t))
        for a in s:
            if a not in hashmapA:
                hashmapA[a] = 1
            else:
                hashmapA[a] += 1
        for b in t:
            if b not in hashmapB:
                hashmapB[b] = 1
            else:
                hashmapB[b] += 1
        for items in hashmapA.items():
            listA.append(items)
        for items in hashmapB.items():
            listB.append(items)

        if listA == listB:
            return True
        else:
            return False  

