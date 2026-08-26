"""All possible combinations - backtracking
    Base Case if path zise is equal to k stop
    Check if no in path dont use
    Action - Append
    Backtracking - Pop"""
"""                if no in path:
                    continue"""
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        path = []

        def repeat(n,k,path,result,start):
            if len(path) == k:
                result.append(path[:])
                return
            
            for no in range(start,n+1):

                path.append(no)
                repeat(n,k,path,result, no + 1)
                path.pop()

        repeat(n,k,path,result, 1)
        return result 

        