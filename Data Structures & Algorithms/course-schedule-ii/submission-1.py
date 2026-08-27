class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        result = []
        visiting = set()
        check = dict()
        for a, b in prerequisites:
            if a not in check:
                check[a] = []
            check[a].append(b)
        
        def dfs(checking, check, result, visiting):
            if checking in result:
                return True
            
            if checking in visiting:
                return False
            else:
                visiting.add(checking)

            if checking in check:
                for a in check[checking]:
                    if not dfs(a, check, result, visiting):
                        return False
            
            visiting.remove(checking)
            result.append(checking)
            return True

        for i in range(numCourses):
            if not dfs(i,check,result, visiting):
                return []
        return result
