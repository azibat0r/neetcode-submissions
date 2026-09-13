class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        a1 = {}
        a2 = {}

        for x in s1:
            if x in a1:
                a1[x] += 1
            else:
                a1[x] = 1

        window = s2[0:len(s1)]       
        
        for x in window:
            if x in a2:
                a2[x] += 1
            else:
                a2[x] = 1 

        if a1 == a2:
            return True            

        for i in range(1,len(s2)-len(s1)+1):
            left = i
            right = i + len(s1)-1

            a2[s2[i-1]] -= 1
            if a2[s2[i-1]] == 0:
                del a2[s2[i-1]]


            if s2[right] in a2:
                a2[s2[right]] += 1
            else:
                a2[s2[right]] = 1 
            

            if a1 == a2:
                return True

        return False




             